# pgzhelper (pgzhelper_rw)

[![PyPI version](https://img.shields.io/pypi/v/pgzhelper_rw.svg)](https://pypi.org/project/pgzhelper_rw/)
[![Documentation Status](https://readthedocs.org/projects/pgzhelper-rw/badge/?version=latest)](https://pgzhelper-rw.readthedocs.io/en/latest/?badge=latest)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

**pgzhelper_rw** is a helper library designed to enhance [Pygame Zero](https://pygame-zero.readthedocs.io/) with Scratch-like intuitive actor capabilities, smooth sprite animations, real-time image manipulations, and comprehensive 2D collision detection algorithms.

---

## 📚 Documentation (라이브러리 레퍼런스)

상세한 한국어/영어/우즈베크어 가이드와 전체 API 레퍼런스는 공식 문서 사이트에서 확인하실 수 있습니다:

👉 **[https://pgzhelper-rw.readthedocs.io](https://pgzhelper-rw.readthedocs.io)**

* **사용자 가이드**: 시작하기, 전체화면 및 마우스 제어
* **Actor 완벽 가이드**: 스크래치 스타일 이동, 각도 회전, 스프라이트 애니메이션, 말풍선(`say`), 붓 궤적(`brush_*`), 실시간 색조 변경(`add_hue`)
* **Collision 가이드**: 점(Point), 선(Line), 원(Circle), AABB 사각형(Rect), 회전 사각형(OBB) 간의 고속 충돌 판정 및 복수형 함수
* **API Reference**: 전체 클래스 및 함수 명세

---

## 🚀 Installation (설치 방법)

Python 3.7 이상 환경에서 `pip`로 설치할 수 있습니다:

```bash
pip install pgzhelper_rw
```

---

## 🎮 Quick Start (기본 사용법)

Pygame Zero 코드에서 `from pgzhelper import *`를 임포트하면 기본 `Actor`가 강화된 `Actor`로 자동 교체됩니다.

```python
import pgzrun
from pgzhelper import *

WIDTH = 800
HEIGHT = 600

alien = Actor('alien')
alien.pos = 400, 300

def update():
    # 1. 마우스 위치를 바라보고 전진 (Scratch 스타일)
    alien.point_towards(pygame.mouse.get_pos())
    alien.move_forward(3)

def draw():
    screen.clear()
    alien.draw()

pgzrun.go()
```

---

## 💡 Key Features (주요 기능)

### 1. Scratch 스타일 Actor 이동 및 회전
```python
actor.move_forward(5)            # 현재 각도 방향으로 전진
actor.move_back(5)               # 후진
actor.move_left(5)               # 좌측 이동 (스트레이프)
actor.move_right(5)              # 우측 이동
actor.point_towards(target)      # 대상 액터 또는 (x, y) 방향 바라보기
actor.distance_to(target)        # 대상과의 거리 계산
actor.move_towards(target, 4)    # 대상을 향해 이동
```

### 2. 스프라이트 애니메이션 & 크기/반전/색조 조절
```python
# 애니메이션
actor.images = ['walk_1', 'walk_2', 'walk_3']
actor.fps = 10
actor.animate()

# 변형 및 색조(Hue) 회전
actor.scale = 1.5                # 크기 확대/축소
actor.flip_x = True              # 좌우 반전
actor.add_hue(30)                # 총알 맞을 때마다 색조 30도씩 변경 (NumPy 가속)
actor.hue = 180                  # 특정 색조 각도 고정
```

### 3. 말풍선 & 이동 궤적 그리기
```python
actor.say("Hello!")              # 머리 위에 말풍선 표시
actor.brush_init((800, 600), thick=3, color='yellow')
actor.brush_start()              # 궤적 그리기 시작
```

### 4. 강력한 충돌 감지 (Collide)
점, 선, 원, 사각형(AABB), 회전 사각형(OBB)을 모두 지원합니다.

```python
from pgzhelper import Collide

# 원과 점 충돌
if Collide.circle_point(cx, cy, radius, px, py):
    print("Hit!")

# 고속 복수형 충돌 (총알 리스트 등)
hit_index = Collide.circle_points(player.x, player.y, player.radius, bullets)
if hit_index != -1:
    del bullets[hit_index]
```

---

## 🌐 Wiki & Resources
* **Official Docs**: [https://pgzhelper-rw.readthedocs.io](https://pgzhelper-rw.readthedocs.io)
* **GitHub Repository**: [https://github.com/roboticsware/pgzhelper](https://github.com/roboticsware/pgzhelper)
* **Original Wiki**: [https://github.com/QuirkyCort/pgzhelper/wiki](https://github.com/QuirkyCort/pgzhelper/wiki)
