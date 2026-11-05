Actor Guide
===========

The ``Actor`` class in ``pgzhelper`` adds numerous Scratch-like movement, animation, and image manipulation capabilities to the Pygame Zero Actor.

Movement & Rotation (Scratch-style)
-----------------------------------

Move and turn actors intuitively:

.. code-block:: python

    # Move forward in the current angle direction
    actor.move_forward(5)

    # Move backwards
    actor.move_back(5)

    # Strafe left / right
    actor.move_left(5)
    actor.move_right(5)

    # Move in an absolute direction angle
    actor.move_in_direction(5)

    # Face towards another actor or (x, y) coordinates
    actor.point_towards(target_actor)
    actor.point_towardsXY(400, 300)

    # Distance and angle calculations
    dist = actor.distance_to(target_actor)
    deg = actor.direction_to(target_actor)

    # Move towards a target (with optional stop on arrival)
    actor.move_towards(target_actor, dist=3, stop_on_target=True)

Image Manipulation & Hue Rotation
---------------------------------

Scale, flip, and dynamically rotate actor color hues:

.. code-block:: python

    # 1. Scale
    actor.scale = 1.5

    # 2. Flip
    actor.flip_x = True   # Horizontal flip
    actor.flip_y = False  # Vertical flip

    # 3. Dynamic Hue Rotation
    # Rotate hue angle by 30 degrees (e.g. on bullet hit)
    actor.add_hue(30)

    # Set specific hue angle (0-360)
    actor.hue = 180

.. note::
   Hue rotation is accelerated with NumPy and cached internally, ensuring 60 FPS performance without stuttering.

Sprite Animation
----------------

Cycle through animation frames seamlessly:

.. code-block:: python

    # Set image frames and frame rate
    actor.images = ['walk_0', 'walk_1', 'walk_2', 'walk_3']
    actor.fps = 10  # 10 frames per second

    def update():
        # Advance animation frame
        actor.animate()

Speech Balloons
---------------

Render speech bubbles above the actor:

.. code-block:: python

    # Display speech text
    actor.say("Hello world!", width=150, height=40, fgcolor='black', bgcolor='white')

    # Clear speech bubble
    actor.say("")

Brush Trail Drawing
-------------------

Leave drawing trails as the actor moves:

.. code-block:: python

    # 1. Initialize brush (screen dimensions, line thickness, color)
    actor.brush_init((800, 600), thick=3, color='yellow')

    # 2. Start drawing
    actor.brush_start()

    # 3. Draw trail in draw() loop
    def draw():
        screen.clear()
        actor.brush_draw()
        actor.draw()

    # 4. Stop and clear
    actor.brush_stop()
    actor.brush_clear()
