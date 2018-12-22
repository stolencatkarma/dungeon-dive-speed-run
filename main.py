import pyglet
import glooey
from src.dungeon import DungeonLevel
from src.player import Player

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


class mainWindow(glooey.containers.Stack):
    def __init__(self):
        super().__init__()
        
        self.current_level = 0
        self.seed = hash('0000000000000000')
        print(self.seed)
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
        self.bg_map_grid = glooey.Grid(0,0,0,0)
        for tile in self.current_room.tiles:
            self.bg_map_grid[tile.x, tile.y] = tile.bg
        self.fg_map_grid = glooey.Grid(0,0,0,0)
        for tile in self.current_room.tiles:
            self.fg_map_grid[tile.x, tile.y] = tile.fg
        # insert mapgrids into our ordered groups.
        self.insert(self.bg_map_grid, 1)
        self.insert(self.fg_map_grid, 2)

        # draw bg of current room
        
        # draw fg of current room
        # draw monsters in current room
        # draw the player 
        # draw player stats
        # draw player skills
    
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