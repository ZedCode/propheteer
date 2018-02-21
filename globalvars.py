import pyglet

# globals.py
#  The one exception to the naming rules laid out in
#  the README are broken here as all globals are always
#  in all caps.

# The primary render batch
RENDER_BATCH = pyglet.graphics.Batch()

# The layer to draw button images on should always
# immediately precede the TEXT_LAYER so we know text
# always has a background if it belongs to a button.
BUTTON_LAYER = pyglet.graphics.OrderedGroup(0)
# The layer text is drawn on, this should always be
# the top layer, so as you need to index additional
# layers, continue to increment this.
TEXT_LAYER = pyglet.graphics.OrderedGroup(1)

# The GAME_WINDOW actually contains useful things
# such as it's own state, so we want to use it throughout.
GAME_WINDOW = pyglet.window.Window(800,600)
