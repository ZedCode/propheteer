# Propheteer Source
This folder is broken up into several folders that you need to understand in order to make changes to this repository.

Path | Contents
---|---
`./main.py` | The entry point to the application.
`./menus.py` | Menu functions and function map.
`./globalvars.py` | A place for global variables for our application. This is a place to set variables and define classes so as not to cause circular imports.
`./config/` | Configuration JSON to be used for application configuration and debugging.
`./pyglet/` | Ignore this folder, this is where the local Python binary lives.
`./resources/` | Image and audio resources.
`./utils/` | Folder for common utilities.
`./utils/config/` | Contains code for loading configuration options and returning appropriate data structures.
`./utils/core.py` | For functions that should be defined outside of game scope to avoid circular dependencies.
`./utils/menu/` | Contains code for drawing / loading menu items.

# Python Style Guide for this Project
For this project, please ensure you follow these coding standards:
- Wrap lines using the guide in Atom.
- Use 4 spaces instead of tab, ensure your IDE is configured to do this automatically.
- Point to the relative Python path instead of starting a virtualenv (e.g. `#!pyglet/bin/python`)
- Use lowerCamelCase variable naming conventions, even in the JSON.
- Use UpperCamelCase for functions we should expect to import into another file.
- Every variable declaration in `./globalvars.py` should be in `ALL_CAPS_WITH_UNDERSCORES`. This is to help denote that this thing is different.

# Preparing your dev environment
Ensure that you have python `virtualenv` installed. Assuming you do, simply clone this repo, go into the folder you cloned and run the following commands `virtualenv pyglet` and `pyglet/bin/pip install pyglet`:
```
$ virtualenv pyglet
Running virtualenv with interpreter /usr/bin/python2
New python executable in pyglet/bin/python2
Also creating executable in pyglet/bin/python
Installing setuptools, pip...done.

$ pyglet/bin/pip install pyglet
Downloading/unpacking pyglet
[...output...]
Successfully installed pyglet future
Cleaning up...
```

The `main.py` file points to the relative `pyglet/bin/python` binary.

# Working with the UI
**NOTE**: This refactor work is in progress right now. It's crudely setup for menus at the moment. It will need to be more refined for the actual "widget" objects as they will need to provide interaction, pieces of information, etc.

Because Pyglet does not provide any graceful UI handling, we will provide our own. Our UI will be based on cutting the screen into a 16x9 grid and then defining x,y values based on this coordinate system. The bottom left spot will be 0,0 all the way up to 15,8:
```
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,8 | 1,8 | 2,8 | 3,8 | 4,8 | 5,8 | 6,8 | 7,8 | 8,8 | 9,8 | 10,8 | 11,8 | 12,8 | 13,8 | 14,8 | 15,8 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,7 | 1,7 | 2,7 | 3,7 | 4,7 | 5,7 | 6,7 | 7,7 | 8,7 | 9,7 | 10,7 | 11,7 | 12,7 | 13,7 | 14,7 | 15,7 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,6 | 1,6 | 2,6 | 3,6 | 4,6 | 5,6 | 6,6 | 7,6 | 8,6 | 9,6 | 10,6 | 11,6 | 12,6 | 13,6 | 14,6 | 15,6 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,5 | 1,5 | 2,5 | 3,5 | 4,5 | 5,5 | 6,5 | 7,5 | 8,5 | 9,5 | 10,5 | 11,5 | 12,5 | 13,5 | 14,5 | 15,5 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,4 | 1,4 | 2,4 | 3,4 | 4,4 | 5,4 | 6,4 | 7,4 | 8,4 | 9,4 | 10,4 | 11,4 | 12,4 | 13,4 | 14,4 | 15,4 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,3 | 1,3 | 2,3 | 3,3 | 4,3 | 5,3 | 6,3 | 7,3 | 8,3 | 9,3 | 10,3 | 11,3 | 12,3 | 13,3 | 14,3 | 15,3 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,2 | 1,2 | 2,2 | 3,2 | 4,2 | 5,2 | 6,2 | 7,2 | 8,2 | 9,2 | 10,2 | 11,2 | 12,2 | 13,2 | 14,2 | 15,2 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,1 | 1,1 | 2,1 | 3,1 | 4,1 | 5,1 | 6,1 | 7,1 | 8,1 | 9,1 | 10,1 | 11,1 | 12,1 | 13,1 | 14,1 | 15,1 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
| 0,0 | 1,0 | 2,0 | 3,0 | 4,0 | 5,0 | 6,0 | 7,0 | 8,0 | 9,0 | 10,0 | 11,0 | 12,0 | 13,0 | 14,0 | 15,0 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+
```

This makes the area of each box as follows for our export from our tool of choice:

Resolution | Size
---|---
1920×1080 | 120x120
1280×720 | 80x80
1024×576 | 64x64

# Suggested Tools

## IDE
For code work, I'm using Atom. As others contribute and end up using their own thing, I will add that here.

## Graphical Applications

### 3D
Should any 3D elements need to be created, **Blender3D** will be used. It is freely available on steam.

### 2D
Background and larger images are done in **Krita** which is freely available. Isometric sprite work is done in **Hexels 3** which is available on Steam.
