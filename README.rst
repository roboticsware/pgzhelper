pgzhelper (pgzhelper_rw)
========================

**pgzhelper_rw** is an enhanced helper library for `Pygame Zero <https://pygame-zero.readthedocs.io/>`_. It brings Scratch-like intuitive actor controls, frame-by-frame sprite animations, real-time image manipulations, and comprehensive 2D collision detection algorithms to your game projects.

Documentation
-------------

Full documentation in **English, 한국어 (Korean), and O'zbekcha (Uzbek)** with tutorials and complete API reference is available at:

👉 **https://pgzhelper-rw.readthedocs.io**

Installation
------------

Requires Python 3.7+ and Pygame Zero 1.2+.

.. code-block:: bash

    pip install pgzhelper_rw

Quick Start
-----------

.. code-block:: python

    import pgzrun
    from pgzhelper import *

    WIDTH = 800
    HEIGHT = 600

    alien = Actor('alien')
    alien.pos = 400, 300

    def update():
        # Point towards mouse and move forward (Scratch style)
        alien.point_towards(pygame.mouse.get_pos())
        alien.move_forward(3)

    def draw():
        screen.clear()
        alien.draw()

    pgzrun.go()

Key Features
------------

* **Scratch-style Movement**: ``move_forward()``, ``point_towards()``, ``distance_to()``, ``move_towards()``
* **Sprite Animation**: Multiple frame cycling with custom ``fps`` (``animate()``)
* **Image Transformation**: Scaling (``scale``), flipping (``flip_x``, ``flip_y``), and real-time hue shifting (``add_hue()``)
* **Speech Balloons & Trail Drawing**: ``say()`` speech bubble rendering and ``brush_*`` path tracing
* **Collision Detection**: Accurate collision checking between Points, Lines, Circles, AABB Rects, and OBB (Oriented Bounding Box) Rects

Resources
---------

* **Documentation**: https://pgzhelper-rw.readthedocs.io
* **GitHub Repository**: https://github.com/roboticsware/pgzhelper
* **PyPI**: https://pypi.org/project/pgzhelper_rw/
* **Original Wiki**: https://github.com/QuirkyCort/pgzhelper/wiki
