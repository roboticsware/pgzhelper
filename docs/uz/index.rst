pgzhelper: Pygame Zero uchun eng zarur yordamchi kutubxona
==========================================================

**pgzhelper (pgzhelper_rw)** — bu `Pygame Zero <https://pygame-zero.readthedocs.io/>`_ imkoniyatlarini kengaytirib, Scratch uslubidagi sodda harakatlarni, rivojlangan to'qnashuvlarni aniqlash (collision detection), animatsiya va tasvirlarni o'zgartirish vositalarini taqdim etuvchi qulay kutubxona.

.. tip::
   🌐 **English Version**: You can find the English version of this documentation in the `docs/en/` directory.
   🌐 **한국어 버전**: Ushbu hujjatning koreyscha versiyasini `docs/` ildiz katalogida topishingiz mumkin.

Asosiy xususiyatlar
-------------------

* **Actor kengaytmalari**:

  * **Scratch uslubidagi harakat**: ``move_forward()``, ``point_towards()``, ``distance_to()``
  * **Spayt animatsiyasi**: Bir nechta kadrlar va ``fps`` bilan oson animatsiya boshqaruvi
  * **Tasvirni o'zgartirish**: O'lchamni kattalashtirish (``scale``), akslantirish (``flip_x``, ``flip_y``) va rang tusini o'zgartirish (``add_hue()``)
  * **Matnli pufakchalar va chizish**: ``say()`` orqali gapirtirish va ``brush_*`` yordamida iz qoldirish

* **Kuchli to'qnashuvlarni aniqlash**:

  * Nuqta (Point), To'g'ri chiziq (Line), Aylana (Circle), To'g'ri to'rtburchak (Rect/AABB) va Burilgan to'rtburchak (OBB) orasidagi to'qnashuvlar
  * Yuqori tezlikda ishlovchi ko'plik funksiyalari (masalan: ``circle_points``, ``obb_lines``)
  * Eng yaqin kesishish nuqtasi koordinatasi va masofasini hisoblash (``line_circle_XY``, ``line_rect_dist``)

* **Foydali vositalar**:

  * To'liq ekran rejimiga o'tish (``toggle_fullscreen``), sichqoncha kursorini yashirish (``hide_mouse``, ``show_mouse``)

O'rnatish
---------

Kutubxonani ``pip`` orqali o'rnatishingiz mumkin:

.. code-block:: bash

    pip install pgzhelper_rw

Tezkor boshlash misoli
----------------------

.. code-block:: python

    import pgzrun
    from pgzhelper import *

    WIDTH = 800
    HEIGHT = 600

    alien = Actor('alien')
    alien.topleft = 100, 100

    def update():
        # Sichqoncha tomon burilish va oldinga harakatlanish
        alien.point_towards(pygame.mouse.get_pos())
        alien.move_forward(3)

    def draw():
        screen.clear()
        alien.draw()

    pgzrun.go()

Mundarija
---------

.. toctree::
   :maxdepth: 2
   :caption: Foydalanuvchi qo'llanmasi

   gettingstarted
   actor
   collision
   api

.. toctree::
   :maxdepth: 1
   :caption: Loyiha haqida

   contributing
   license
