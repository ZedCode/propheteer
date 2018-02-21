import pyglet

# core.py
#  These utilities do not belong to any specific
#  module or class, but rather are generally
#  used in game setup.

# This should pretty much be used on every
# resource.
def CenterImage(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2
