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
**NOTE**: This refactor work is in progress right now, and everything under `utils/menu` needs to be updated to work like this instead of how it's currently working.

Because Pyglet does not provide any graceful UI handling, we will provide our own. Our UI will be based on cutting the screen into a 8x8 grid and then defining x,y values based on this coordinate system. The upper left spot will be 0,0 all the way down to 7,7:
```
+-----+-----+-----+-----+-----+-----+-----+-----+
| 0,0 | 1,0 | 2,0 | 3,0 | 4,0 | 5,0 | 6,0 | 7,0 |
+-----+-----+-----+-----+-----+-----+-----+-----+
| 0,1 | 1,1 | 2,1 | 3,1 | 4,1 | 5,1 | 6,1 | 7,1 |
+-----+-----+-----+-----+-----+-----+-----+-----+
| 0,2 | 1,2 | 2,2 | 3,2 | 4,2 | 5,2 | 6,2 | 7,2 |
+-----+-----+-----+-----+-----+-----+-----+-----+
| 0,3 | 1,3 | 2,3 | 3,3 | 4,3 | 5,3 | 6,3 | 7,3 |
+-----+-----+-----+-----+-----+-----+-----+-----+
| 0,4 | 1,4 | 2,4 | 3,4 | 4,4 | 5,4 | 6,4 | 7,4 |
+-----+-----+-----+-----+-----+-----+-----+-----+
| 0,5 | 1,5 | 2,5 | 3,5 | 4,5 | 5,5 | 6,5 | 7,5 |
+-----+-----+-----+-----+-----+-----+-----+-----+
| 0,6 | 1,6 | 2,6 | 3,6 | 4,6 | 5,6 | 6,6 | 7,6 |
+-----+-----+-----+-----+-----+-----+-----+-----+
| 0,7 | 1,7 | 2,7 | 3,7 | 4,7 | 5,7 | 6,7 | 7,7 |
+-----+-----+-----+-----+-----+-----+-----+-----+
```

This makes the area of each box as follows for our export from our tool of choice:

Resolution | Size
---|---
1024x768 | 128x96
800x600 | 100x60
640x480 | 80x60

# Suggested Tools

## IDE
For code work, I'm using Atom. As others contribute and end up using their own thing, I will add that here.

## Graphical Applications

### 3D
Should any 3D elements need to be created, **Blender3D** will be used. It is freely available on steam.

### 2D
Background and larger images are done in **Krita** which is freely available. Isometric sprite work is done in **Hexels 3** which is available on Steam.
