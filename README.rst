pgzhelper (pgzhelper_rw)
========================

**pgzhelper_rw** is a helper library designed to enhance `Pygame Zero <https://pygame-zero.readthedocs.io/>`_ with Scratch-like intuitive actor capabilities, smooth sprite animations, real-time image manipulations, and comprehensive 2D collision detection algorithms.

Documentation
-------------

Detailed guides (in Korean, English, and Uzbek) and full API reference are available at:

👉 **https://pgzhelper-rw.readthedocs.io**

Installation
------------

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
        alien.point_towards(pygame.mouse.get_pos())
        alien.move_forward(3)

    def draw():
        screen.clear()
        alien.draw()

    pgzrun.go()

Resources
---------

* **Documentation**: https://pgzhelper-rw.readthedocs.io
* **GitHub**: https://github.com/roboticsware/pgzhelper
* **Original Wiki**: https://github.com/QuirkyCort/pgzhelper/wiki
