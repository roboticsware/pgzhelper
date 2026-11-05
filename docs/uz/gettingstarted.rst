Ishni boshlash
==============

O'rnatish
---------

``pgzhelper_rw`` Python 3.7+ va Pygame Zero 1.2+ versiyalarini qo'llab-quvvatlaydi.

.. code-block:: bash

    pip install pgzhelper_rw

Asosiy tuzilma
--------------

Pygame Zero loyihangizda ``pgzhelper`` kutubxonasini import qilsangiz, standart ``Actor`` avtomatik ravishda kengaytirilgan imkoniyatlarga ega bo'ladi.

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

Ekran va sichqoncha boshqaruvi
------------------------------

To'liq ekran rejimiga o'tish yoki sichqoncha kursorini yashirish juda oson:

.. code-block:: python

    from pgzhelper import toggle_fullscreen, hide_mouse, show_mouse

    # To'liq ekranga o'tish
    toggle_fullscreen()

    # Sichqoncha kursorini yashirish
    hide_mouse()
