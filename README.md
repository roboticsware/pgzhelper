# pgzhelper (pgzhelper_rw)

[![PyPI version](https://img.shields.io/pypi/v/pgzhelper_rw.svg)](https://pypi.org/project/pgzhelper_rw/)
[![Documentation Status](https://readthedocs.org/projects/pgzhelper-rw/badge/?version=latest)](https://pgzhelper-rw.readthedocs.io/en/latest/?badge=latest)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

**pgzhelper_rw** is an enhanced helper library for [Pygame Zero](https://pygame-zero.readthedocs.io/). It brings Scratch-like intuitive actor controls, frame-by-frame sprite animations, real-time image manipulations, and comprehensive 2D collision detection algorithms to your game projects.

---

## 📚 Documentation / 공식 문서

Full documentation in **English, 한국어 (Korean), and O'zbekcha (Uzbek)** with comprehensive API references and tutorials is available at:

👉 **[https://pgzhelper-rw.readthedocs.io](https://pgzhelper-rw.readthedocs.io)**

* **User Guides**: Getting started, screen controls (fullscreen/windowed), and mouse visibility.
* **Actor Complete Guide**: Scratch-style movement (`move_forward`, `point_towards`), sprite animation, speech balloons (`say`), trail drawing (`brush_*`), and dynamic hue shifting (`add_hue`).
* **Collision Guide**: Collision detection between Points, Lines, Circles, AABB Rectangles, and OBB (Oriented Bounding Box) Rectangles, with high-performance plural query functions.
* **API Reference**: Detailed class and function specifications.

---

## 🚀 Installation / 설치

Requires Python 3.7+ and Pygame Zero 1.2+. Install from PyPI via `pip`:

```bash
pip install pgzhelper_rw
```

---

## 🎮 Quick Start / 빠른 시작

Importing `pgzhelper` automatically enhances Pygame Zero's standard `Actor` class with extra superpowers.

```python
import pgzrun
from pgzhelper import *

WIDTH = 800
HEIGHT = 600

alien = Actor('alien')
alien.pos = 400, 300

def update():
    # 1. Look towards the mouse position and move forward (Scratch style)
    alien.point_towards(pygame.mouse.get_pos())
    alien.move_forward(3)

def draw():
    screen.clear()
    alien.draw()

pgzrun.go()
```

---

## 💡 Key Features / 주요 기능

### 1. Scratch-style Actor Movements / 직관적인 이동 및 회전
```python
actor.move_forward(5)            # Move forward in the direction of current angle
actor.move_back(5)               # Move backward
actor.move_left(5)               # Strafe left
actor.move_right(5)              # Strafe right
actor.point_towards(target)      # Point towards another actor or (x, y) coordinates
actor.distance_to(target)        # Calculate distance to target
actor.move_towards(target, 4)    # Move directly towards target
```

### 2. Sprite Animation & Image Effects / 애니메이션 및 이미지 효과
```python
# Frame-by-frame sprite animation
actor.images = ['walk_1', 'walk_2', 'walk_3']
actor.fps = 10
actor.animate()

# Scaling & Flipping
actor.scale = 1.5                # Scale sprite size
actor.flip_x = True              # Flip horizontally
actor.flip_y = False             # Flip vertically

# Real-time Hue Rotation (NumPy accelerated & cached)
actor.add_hue(30)                # Shift color hue by +30 degrees (e.g. on bullet hit)
actor.hue = 180                  # Set specific hue angle (0 ~ 360)
```

### 3. Speech Balloons & Trail Drawing / 말풍선 및 궤적 그리기
```python
# Display speech bubble above the actor
actor.say("Hello World!", width=150, height=40, fgcolor='black', bgcolor='white')

# Brush trail drawing as the actor moves
actor.brush_init((800, 600), thick=3, color='yellow')
actor.brush_start()
```

### 4. Comprehensive Collision Detection (Collide) / 강력한 충돌 감지
Supports accurate collision checks between Points, Lines, Circles, AABB Rectangles, and OBB (rotated) Rectangles.

```python
from pgzhelper import Collide

# Single collision check: Circle vs Point
if Collide.circle_point(cx, cy, radius, px, py):
    print("Collision detected!")

# High-performance plural collision check: Circle vs list of Points (e.g. bullets)
hit_index = Collide.circle_points(player.x, player.y, player.radius, bullets)
if hit_index != -1:
    print(f"Hit by bullet index: {hit_index}")
    del bullets[hit_index]
```

---

## 🌐 Resources & Links
* **Official Documentation**: [https://pgzhelper-rw.readthedocs.io](https://pgzhelper-rw.readthedocs.io)
* **GitHub Repository**: [https://github.com/roboticsware/pgzhelper](https://github.com/roboticsware/pgzhelper)
* **PyPI Package**: [https://pypi.org/project/pgzhelper_rw/](https://pypi.org/project/pgzhelper_rw/)
* **Original pgzhelper Wiki**: [https://github.com/QuirkyCort/pgzhelper/wiki](https://github.com/QuirkyCort/pgzhelper/wiki)
