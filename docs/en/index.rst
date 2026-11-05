pgzhelper: Essential Helper Library for Pygame Zero
===================================================

**pgzhelper (pgzhelper_rw)** enhances `Pygame Zero <https://pygame-zero.readthedocs.io/>`_ with intuitive Scratch-like actor controls, advanced collision detection, animations, and image manipulations.

Key Features
------------

* **Actor Enhancements**:

  * **Scratch-style Movement**: ``move_forward()``, ``point_towards()``, ``distance_to()``
  * **Sprite Animation**: Multiple frame cycling with custom ``fps``
  * **Image Transformation**: Scaling (``scale``), flipping (``flip_x``, ``flip_y``), and real-time hue shifting (``add_hue()``)
  * **Speech Bubbles & Trail Drawing**: Render speech balloons with ``say()`` and trace paths using ``brush_*``

* **Powerful Collision Detection**:

  * Accurate collision checking between Points, Lines, Circles, AABB Rectangles, and OBB (Oriented Bounding Box) Rectangles
  * High-performance plural functions (e.g. ``circle_points``, ``obb_lines``)
  * Distance and coordinate reporting (e.g. ``line_circle_XY``, ``line_rect_dist``)

* **Utilities**:

  * Fullscreen toggle (``toggle_fullscreen``), mouse cursor visibility (``hide_mouse``, ``show_mouse``)

Installation
------------

.. code-block:: bash

    pip install pgzhelper_rw

Quick Example
-------------

.. code-block:: python

    import pgzrun
    from pgzhelper import *

    WIDTH = 800
    HEIGHT = 600

    alien = Actor('alien')
    alien.topleft = 100, 100

    def update():
        alien.point_towards(pygame.mouse.get_pos())
        alien.move_forward(3)

    def draw():
        screen.clear()
        alien.draw()

    pgzrun.go()

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   gettingstarted
   actor
   collision
   api

.. toctree::
   :maxdepth: 1
   :caption: Project Info

   contributing
   license
