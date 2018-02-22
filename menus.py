import pyglet, os, sys
from utils.core import CenterImage
from utils.config.jsonloader import LoadData
from utils.menu.menu import menu
from globalvars import RENDER_BATCH, BUTTON_LAYER, TEXT_LAYER, GAME_WINDOW, UI_WIDTH, UI_HEIGHT
# menus.py
#  Contains the code to support menu
#  functionality.

# We first need all of the menu data
menuFromJSON = LoadData(os.path.join(os.path.dirname(__file__), 'config', 'menus.json'))

# In order to prevent circular imports we
# should implement our own resource loader
# specifically for Menus. The dict key names
# should match what's in the JSON.
buttonLongBlue = pyglet.image.load(os.path.join(os.path.dirname(__file__),
    'resources',
    'buttonLong_blue.png'))
buttonLongBluePressed = pyglet.image.load(os.path.join(os.path.dirname(__file__),
    'resources',
    'buttonLong_blue_pressed.png'))
CenterImage(buttonLongBlue)
CenterImage(buttonLongBluePressed)
MenuButtonImages = {
    'buttonLongBlue': buttonLongBlue,
    'buttonLongBluePressed': buttonLongBluePressed
}
# MENU FUNCTIONS
#  When adding new menu / menu options, ensure
#  that they have function map entries. These
#  functions should not be called directly but
#  only as part of the MenuMap dict built below.
def newGameMenu():
    print("Inside of newGameMenu function. Not implemented.")

def optionsMenu():
    for i in AllMenus:
        AllMenus[i].hide()
    AllMenus['OptionsMenu'].show()
    AllMenus['OptionsMenu'].menuTitle("Options")

def quitConfirmMenu():
    for i in AllMenus:
        AllMenus[i].hide()
    AllMenus['QuitConfirmMenu'].show()
    AllMenus['QuitConfirmMenu'].menuTitle("Are you Sure?")

def mainMenu():
    for i in AllMenus:
        AllMenus[i].hide()
    AllMenus['MainMenu'].show()
    AllMenus['MainMenu'].menuTitle("Main Menu")



def quitGame():
    # Hide all menus and quit game.
    for i in AllMenus:
        AllMenus[i].hide()
    sys.exit()


# MenuMapFunctions
#  This holds all of our functions in a dict
#  so that we can access their functionality
#  more directly from the JSON.
MenuMapFunctions = {
    'newGameMenu': newGameMenu,
    'optionsMenu': optionsMenu,
    'quitConfirmMenu': quitConfirmMenu,
    'mainMenu': mainMenu,
    'quitGame': quitGame
}

# GameMenus will be a single dict which will contain
# each of our menu object instances built with the
# data above. What good is storing all this in JSON
# for easy re-use if we manually code everything?
AllMenus = {}
for i in menuFromJSON['menus']:
    AllMenus[str(i['menu']['name']).replace(" ","")] = menu(
        x=(GAME_WINDOW.width / UI_WIDTH) * i['menu']['x'],
        y=(GAME_WINDOW.height / UI_HEIGHT) * i['menu']['y'],
        buttonLayer=BUTTON_LAYER,
        textLayer=TEXT_LAYER,
        renderBatch=RENDER_BATCH,
        buttonUp=MenuButtonImages[str(i['menu']['buttonUp'])],
        buttonDown=MenuButtonImages[str(i['menu']['buttonDown'])],
        horizontal=i['menu']['horizontal']
    )
for i in menuFromJSON['menus']:
    for f in i['menu']['items']:
        AllMenus[str(i['menu']['name']).replace(" ","")].add(str(f['name']),
        MenuMapFunctions[str(f['function'])])
for i in AllMenus:
    AllMenus[i].makeLabels()
    AllMenus[i].hide()
