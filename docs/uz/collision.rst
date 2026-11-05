To'qnashuvlar qo'llanmasi
=========================

``pgzhelper`` 5 xil geometrik shakl orasida aniq va tezkor to'qnashuvlarni aniqlash funksiyalarini taqdim etadi.

Mavjud shakllar
---------------

* **Point (Nuqta)**: O'qlar kabi juda kichik ob'ektlar
* **Line (To'g'ri chiziq)**: Lazerlar, traektoriyalar va to'siqlar
* **Circle (Aylana)**: O'yinchilar, qalqonlar va zarrachalar
* **Rect (AABB to'rtburchak)**: O'qlar bo'ylab joylashgan (burilmagan) to'rtburchaklar
* **OBB (Burilgan to'rtburchak)**: Istalgan burchakka burilgan to'rtburchaklar

Asosiy foydalanish
------------------

To'qnashuv funksiyalari ``Collide`` sinfida statik metodlar sifatida joylashgan:

.. code-block:: python

    from pgzhelper import Collide

    if Collide.circle_point(circle_x=300, circle_y=200, radius=50, point_x=320, point_y=180):
        print("To'qnashuv aniqlandi!")

Aktyor uchun qulay metodlar
---------------------------

``Actor`` sinfida ham to'g'ridan-to'g'ri chaqirish mumkin bo'lgan metodlar mavjud:

.. code-block:: python

    # Aylana to'qnashuvi
    player.circle_collidecircle(enemy)
    player.circle_colliderect(wall)
    player.circle_collidepoint(mouse_x, mouse_y)

    # OBB (burilgan to'rtburchak) to'qnashuvi
    player.obb_collideobb(rotated_box)
    player.obb_collidepoint(bullet_x, bullet_y)

Ko'plik shakllari (Yuqori unumdorlik)
-------------------------------------

Ko'p sonli nishonlar (masalan, 50 ta o'q koordinatasi) bilan tekshirishda ko'plik funksiyalarini chaqirish tsikldan ko'ra ancha tez ishlaydi.
Ular to'qnashgan birinchi elementning **indeksini (0-based)** qaytaradi, to'qnashuv bo'lmasa ``-1`` qaytadi:

.. code-block:: python

    bullets = [(100, 150), (200, 250), (300, 350)]

    hit_index = Collide.circle_points(player.x, player.y, player.radius, bullets)
    if hit_index != -1:
        print(f"{hit_index}-raqamli o'q tegdi!")
        del bullets[hit_index]

Chiziq kesishish nuqtasi va masofa
----------------------------------

Reykasting (raycasting) va traektoriyalarni aniqlash uchun foydali:

* ``line_circle_XY(x1, y1, x2, y2, cx, cy, cr)``: Birinchi kesishish nuqtasi ``(x, y)`` koordinatasini qaytaradi.
* ``line_rect_dist(x1, y1, x2, y2, rx, ry, rw, rh)``: ``(x1, y1)`` dan to'qnashuv nuqtasigacha bo'lgan masofani qaytaradi.
* ``line_rect_dist_squared(...)``: Masofaning kvadratini qaytaradi (ildiz hisoblanmagani uchun eng tezi).
