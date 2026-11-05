Getting Started
===============

Installation
------------

``pgzhelper_rw`` supports Python 3.7+ and Pygame Zero 1.2+.

.. code-block:: bash

    pip install pgzhelper_rw

Basic Structure
---------------

Importing ``pgzhelper`` in your Pygame Zero program automatically replaces the standard ``Actor`` with an enhanced one.

.. code-block:: python

    import pgzrun
    from pgzhelper import *

    WIDTH = 640
    HEIGHT = 480

    player = Actor('character')
    player.pos = 320, 240

    def update():
        if keyboard.left:
            player.move_left(4)
        if keyboard.right:
            player.move_right(4)

    def draw():
        screen.clear()
        player.draw()

    pgzrun.go()

Screen & Mouse Controls
-----------------------

Easily toggle fullscreen mode or toggle mouse cursor visibility:

.. code-block:: python

    from pgzhelper import toggle_fullscreen, hide_mouse, show_mouse

    # Toggle fullscreen mode
    toggle_fullscreen()

    # Hide mouse cursor
    hide_mouse()
