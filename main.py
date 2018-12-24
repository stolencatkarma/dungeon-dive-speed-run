import pyglet
import glooey
from src.dungeon import DungeonLevel
from src.player import Player
import random

for folder in [
    # load tileset resources
    "tiles/bg",
    "tiles/fg",
    "tiles/characters",
    "tiles/monsters",
    "tiles/items",
    "tiles/monsters",

    # load UI graphicss
    "gfx/inputbox",
    "gfx/background",
    "gfx/scrollbox/vbar/backward",
    "gfx/scrollbox/vbar/forward",
    "gfx/scrollbox/vbar/decoration",
    "gfx/scrollbox/vbar/grip",
    "gfx/scrollbox/frame/decoration",
]:
    pyglet.resource.path.append(folder)
    print("Loaded resource folder", folder)
pyglet.resource.reindex()


class CustomBackground(glooey.Background):
    custom_center = pyglet.resource.texture('center.png')
    custom_top = pyglet.resource.texture('top.png')
    custom_bottom = pyglet.resource.texture('bottom.png')
    custom_left = pyglet.resource.texture('left.png')
    custom_right = pyglet.resource.texture('right.png')
    custom_top_left = pyglet.resource.image('top_left.png')
    custom_top_right = pyglet.resource.image('top_right.png')
    custom_bottom_left = pyglet.resource.image('bottom_left.png')
    custom_bottom_right = pyglet.resource.image('bottom_right.png')

class StatsBox(glooey.Bin):
    def __init__(self):
        super().__init__()
        self.grid = glooey.Grid(0,0,0,0)
        self.grid[0,0] = glooey.dialogs.Label('hp')
        self.grid[1,0] = glooey.dialogs.Label('str')
        self.grid[2,0] = glooey.dialogs.Label('spd')
        self.grid[3,0] = glooey.dialogs.Label('int')
        self.grid[4,0] = glooey.dialogs.Label('res')
        self.grid[5,0] = glooey.dialogs.Label('tgt')
        self.add(self.grid)

class SkillsBox(glooey.Bin):
    def __init__(self, skill1, skill2):
        super().__init__()
        self.grid = glooey.Grid(0,0,0,0)
        self.grid[0,0] = skill1.image
        self.grid[0,1] = skill2.image

        self.add(self.grid)
        


class mainWindow(glooey.containers.Stack):
    def __init__(self):
        super().__init__()

        self.current_level = 0
        self.seed = random.randint(1000000000000000,9000000000000000)
        print('using seed', str(self.seed))
        self.current_room_x = 2
        self.current_room_y = 2
        self.current_room = None
        self.dungeon = dict()
        self.dungeon[self.current_level] = DungeonLevel(self.current_level)
        self.player = Player()
        # setup player according to chosen starting weapon and stats

        # find the current room the player is in
        for room in self.dungeon[self.current_level].rooms:
            if room.x == self.current_room_x:
                if room.y == self.current_room_y:
                    self.current_room = room

        # insert our custom Background into an OrderedGroup
        self.insert(CustomBackground(), 0)

        # init and fill mapgrids.
        self.bg_map_grid = glooey.Grid(0, 0, 0, 0)
        for tile in self.current_room.tiles:
            # draw bg of current room
            self.bg_map_grid[tile.x, tile.y] = glooey.Image(tile.bg)

        self.fg_map_grid = glooey.Grid(0, 0, 0, 0)
        for tile in self.current_room.tiles:
            # draw fg of current room
            self.fg_map_grid[tile.x, tile.y] = glooey.Image(tile.fg)

        # insert mapgrids into our ordered groups.
        self.insert(self.bg_map_grid, 1)
        self.insert(self.fg_map_grid, 2)

        # draw monsters and player on a grid
        self.creature_map_grid = glooey.Grid(0, 0, 0, 0)
        for creature in self.current_room.characters:
            self.creature_map_grid[creature.x, creature.y] = creature.image
        
        self.insert(self.creature_map_grid, 3)

        # draw player stats
        self.stats_box = StatsBox()
        self.insert(self.stats_box, 4)

        # draw player skills
        # skill1, skill2

    def redraw(self):
        pass


class Main:
    def __init__(self):
        self.window = pyglet.window.Window(1024, 768)
        self.window.set_location(0, 32)

        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA,
                              pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

        self.gui = glooey.Gui(self.window)

        self.gui.add(mainWindow())


if __name__ == "__main__":

    main = Main()

    pyglet.app.event_loop.run()  # main event loop starts here.
