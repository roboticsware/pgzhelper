Collision Guide
===============

``pgzhelper`` provides accurate, high-performance collision functions between 5 distinct geometric shapes.

Available Shapes
----------------

* **Point**: Tiny objects like bullets
* **Line**: Lasers, trajectories, and obstacles
* **Circle**: Players, circular shields, and particles
* **Rect (AABB)**: Axis-Aligned Bounding Box (unrotated boxes/tiles)
* **OBB**: Oriented Bounding Box (rectangles rotated to arbitrary angles)

Basic Usage
-----------

Collision methods are available as static methods on the ``Collide`` class:

.. code-block:: python

    from pgzhelper import Collide

    if Collide.circle_point(circle_x=300, circle_y=200, radius=50, point_x=320, point_y=180):
        print("Collision detected!")

Actor Collision Methods
-----------------------

The ``Actor`` class includes built-in collision shortcuts:

.. code-block:: python

    # Circle collision
    player.circle_collidecircle(enemy)
    player.circle_colliderect(wall)
    player.circle_collidepoint(mouse_x, mouse_y)

    # OBB (oriented box) collision
    player.obb_collideobb(rotated_box)
    player.obb_collidepoint(bullet_x, bullet_y)

Plural Forms (High Performance)
-------------------------------

When checking collision against a list of objects (e.g. 50 bullets), plural functions are much faster than iterating with singular functions.
They return the **0-based index** of the first colliding element, or ``-1`` if none collide:

.. code-block:: python

    bullets = [(100, 150), (200, 250), (300, 350)]

    hit_index = Collide.circle_points(player.x, player.y, player.radius, bullets)
    if hit_index != -1:
        print(f"Hit by bullet index {hit_index}!")
        del bullets[hit_index]

Line Intersection Coordinates & Distance
----------------------------------------

Useful for raycasting and bullet trajectory tests:

* ``line_circle_XY(x1, y1, x2, y2, cx, cy, cr)``: Returns ``(x, y)`` of the first intersection point (or ``(None, None)``).
* ``line_rect_dist(x1, y1, x2, y2, rx, ry, rw, rh)``: Returns direct distance from ``(x1, y1)`` to intersection.
* ``line_rect_dist_squared(...)``: Returns squared distance (avoids square root, fastest).
