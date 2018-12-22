import pyglet
import glooey

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

class mainWindow(glooey.containers.Stack):
    def __init__(self):
        super().__init__()

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