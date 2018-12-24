import glooey
import pyglet


class DungeonLevel:
    def __init__(self, depth):
        self.rooms = list()
        # pair of up/down stairs always in the center
        # boss rooms have their own entrance and exits.

        # when we create a new dungon level we need to be aware of a few things.
        # depth, and whether it's a boss level or not.

        # now that we've initialized the level we need to build it.
        # then add monsters to fight
        # then items to interact with.

        # make 5 'rooms' wide and 5 'rooms' high
        for i in range(5):
            for j in range(5):
                _room = Room(i, j, depth)
                self.rooms.append(_room)


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.impassible = 0
        self.bg = pyglet.resource.texture("floor1.png")
        # fg can be blank or an item/object.
        self.fg = pyglet.resource.texture("blank.png")


class Room:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.tiles = list()
        self.characters = list()
        self.items = list()
        self.exits = list()

        # used in difficulty calculations
        self.depth = depth

        # A room is part of a dungeon with exits to other rooms.
        # the player only can move in a 5x5 area and has to think tactically to defeat or avoid monsters in the least amount of moves.
        for i in range(7):
            for j in range(7):
                _tile = Tile(i, j)
                if(i == 0 or i == 6):
                    _tile.impassible = 1
                    if(i == 0 and j == 0):
                        _tile.bg = pyglet.resource.texture("TL_wall.png")
                    elif(i == 6 and j == 0):
                        _tile.bg = pyglet.resource.texture("TR_wall.png")
                    elif(i == 0 and j == 6):
                        _tile.bg = pyglet.resource.texture("BL_wall.png")
                    elif(i == 6 and j == 6):
                        _tile.bg = pyglet.resource.texture("BR_wall.png")
                    elif(i == 0 or i == 6):
                        _tile.bg = pyglet.resource.texture("horz_wall.png")
                    else:
                        _tile.bg = pyglet.resource.texture("vert_wall.png")
                if(j == 0 or j == 6):
                    _tile.impassible = 1
                if(x == 3 and y == 3):  # center room needs stairs.
                    if(i == 2 and j == 3):
                        _tile.bg = pyglet.resource.texture("stairs_down.png")
                    if(i == 4 and j == 3):
                        _tile.bg = pyglet.resource.texture("stairs_up.png")
                self.tiles.append(_tile)
        # generate exits
        # generate monsters
        # generate items

