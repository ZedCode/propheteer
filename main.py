#!pyglet/bin/python
import pyglet, os, sys
from globalvars import GAME_WINDOW, RENDER_BATCH, BACKGROUND_LAYER
from menus import AllMenus, mainMenu


# Propheteer main.py
#
# This file should merely be the entry point into the game. It should bring
# in the necessary imports to start the game.



# Event code should be kept to a minimum and instead
# should just iterate over objects which need to be
# updated at each tick.
@GAME_WINDOW.event
def on_draw():
    GAME_WINDOW.clear()
    RENDER_BATCH.draw()

# To interact with menu objects, we need
# to capture mouse presses/events
@GAME_WINDOW.event
def on_mouse_press(x, y, button, modifiers):
    for i in AllMenus:
        for k,v in AllMenus[i].menuItems.iteritems():
            if k in AllMenus[i].readableLabels:
                if v[0].checkPress(x,y):
                    v[0].downImage()

@GAME_WINDOW.event
def on_mouse_release(x, y, button, modifiers):
    functionsToFire = []
    for i in AllMenus:
        for k,v in AllMenus[i].menuItems.iteritems():
            if k in AllMenus[i].readableLabels:
                if v[0].checkPress(x,y):
                    functionsToFire.append(v[1])
    for i in functionsToFire:
        i()
    for i in AllMenus:
        for k,v in AllMenus[i].menuItems.iteritems():
            v[0].upImage()

if __name__ == '__main__':
    # We can kick off the rest of the entire game from showing the main menu.
    mainMenu()

    # Load the background image
    #  This should be broken out into some sort of loading module that can
    #  figure out assets to load and handle things more gracefully.
    BackgroundImage = pyglet.image.load(os.path.join(os.path.dirname(__file__),
        'resources',
        'background_576p.png'))
    BackgroundSprite = pyglet.sprite.Sprite(img=BackgroundImage, x=0, y=0)
    BackgroundSprite.batch = RENDER_BATCH
    BackgroundSprite.group = BACKGROUND_LAYER

    # Finally, start the application
    pyglet.app.run()
