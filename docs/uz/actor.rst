Actor qo'llanmasi
=================

``pgzhelper`` dagi ``Actor`` sinfi Pygame Zero dasturchilariga Scratch uslubidagi qulay harakat, animatsiya va tasvirlarni boshqarish imkonini beradi.

Harakat va burilish (Scratch uslubi)
------------------------------------

Aktyorni intuitiv ravishda harakatlantirish va yo'naltirish mumkin:

.. code-block:: python

    # Joriy burchak yo'nalishi bo'yicha oldinga harakatlanish
    actor.move_forward(5)

    # Orqaga harakatlanish
    actor.move_back(5)

    # Chapga / o'ngga yonlama harakatlanish
    actor.move_left(5)
    actor.move_right(5)

    # Mutlaq burchak yo'nalishida harakatlanish
    actor.move_in_direction(5)

    # Boshqa aktyor yoki (x, y) koordinatasiga burilish
    actor.point_towards(target_actor)
    actor.point_towardsXY(400, 300)

    # Masofa va yo'nalish burchagini hisoblash
    dist = actor.distance_to(target_actor)
    deg = actor.direction_to(target_actor)

    # Belgilangan nishonga tomon harakatlanish (yetib borganda to'xtash)
    actor.move_towards(target_actor, dist=3, stop_on_target=True)

Tasvir o'lchami va rang tusini o'zgartirish
-------------------------------------------

O'lchamni o'zgartirish, akslantirish va rang tusini o'zgartirish:

.. code-block:: python

    # 1. O'lcham (masshtab)
    actor.scale = 1.5

    # 2. Gorizontal va vertikal akslantirish
    actor.flip_x = True   # Gorizontal akslantirish
    actor.flip_y = False  # Vertikal akslantirish

    # 3. Rang tusini o'zgartirish (Hue)
    # Masalan, o'q tekkanda rang tusini 30 gradusga surish
    actor.add_hue(30)

    # Rang burchagini aniq belgilash (0-360)
    actor.hue = 180

.. note::
   Rang tusini o'zgartirish NumPy yordamida tezlashtirilgan va keshlanadi, bu o'yinda qotishlarsiz 60 FPS ishlashni ta'minlaydi.

Spayt animatsiyasi
------------------

Bir nechta kadrlarni ketma-ket almashtirish:

.. code-block:: python

    # Kadrlar ro'yxati va tezlik (fps)
    actor.images = ['walk_0', 'walk_1', 'walk_2', 'walk_3']
    actor.fps = 10  # Soniyasiga 10 kadr

    def update():
        # Animatsiya kadrini oldinga surish
        actor.animate()

Nutq pufakchalari (Say)
-----------------------

Aktyor boshida matnli pufakchani ko'rsatish:

.. code-block:: python

    # Matn va pufakcha o'lchamini berish
    actor.say("Salom dunyo!", width=150, height=40, fgcolor='black', bgcolor='white')

    # Nutq pufakchasini o'chirish
    actor.say("")

Mo'yqalam bilan iz qoldirish (Brush)
------------------------------------

Aktyor harakati ortidan chiziq chizib borish:

.. code-block:: python

    # 1. Mo'yqalamni ishga tushirish (ekran o'lchami, qalinlik, rang)
    actor.brush_init((800, 600), thick=3, color='yellow')

    # 2. Chizishni boshlash
    actor.brush_start()

    # 3. draw() ichida chiziqni aks ettirish
    def draw():
        screen.clear()
        actor.brush_draw()
        actor.draw()

    # 4. To'xtatish va tozalash
    actor.brush_stop()
    actor.brush_clear()
