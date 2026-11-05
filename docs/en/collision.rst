충돌 감지 가이드 (Collision Guide)
===================================

``pgzhelper`` 는 게임 개발에 필요한 5가지 기하학적 형태 간의 정밀하고 빠른 충돌 판정 함수들을 제공합니다.

지원하는 도형
-------------

* **Point (점)**: 총알 등 크기가 매우 작은 객체
* **Line (선)**: 레이저, 발사체 궤적, 벽면
* **Circle (원)**: 캐릭터, 구체, 폭발 반경
* **Rect (AABB 직사각형)**: 축에 평행한 사각형 (회전하지 않는 플랫폼, 블록)
* **OBB (회전 직사각형)**: 임의의 각도로 회전된 지형 및 스프라이트

기본 사용법
-----------

충돌 판정 함수는 ``Collide`` 클래스의 정적 메서드로 제공됩니다.

.. code-block:: python

    from pgzhelper import Collide

    # 원과 점 충돌 검사
    if Collide.circle_point(circle_x=300, circle_y=200, radius=50, point_x=320, point_y=180):
        print("충돌!")

액터 간 편리한 충돌 메서드
--------------------------

``Actor`` 클래스에도 다음과 같은 충돌 편의 메서드가 내장되어 있습니다:

.. code-block:: python

    # 원형 충돌
    player.circle_collidecircle(enemy)
    player.circle_colliderect(wall)
    player.circle_collidepoint(mouse_x, mouse_y)

    # 회전 사각형(OBB) 충돌
    player.obb_collideobb(rotated_box)
    player.obb_collidepoint(bullet_x, bullet_y)

복수형 판정 (Plural Form)
-------------------------

많은 수의 객체(예: 50개의 총알 좌표 리스트)와 충돌을 검사할 때는 단수형을 루프로 돌리는 것보다 복수형 함수를 사용하는 것이 훨씬 빠릅니다.
복수형 함수는 가장 먼저 충돌한 대상의 **인덱스(0-based)**\ 를 반환하며, 충돌이 없으면 ``-1``\ 을 반환합니다.

.. code-block:: python

    bullets = [(100, 150), (200, 250), (300, 350)]

    hit_index = Collide.circle_points(player.x, player.y, player.radius, bullets)
    if hit_index != -1:
        print(f"{hit_index}번째 총알에 피격되었습니다!")
        del bullets[hit_index]

선(Line) 교차 지점 및 거리 계산
-------------------------------

레이캐스팅이나 총알 관통 궤적 판정에 유용한 함수들입니다:

* ``line_circle_XY(x1, y1, x2, y2, cx, cy, cr)``: 첫 번째 충돌 지점의 ``(x, y)`` 좌표를 반환 (충돌 없으면 ``(None, None)``)
* ``line_rect_dist(x1, y1, x2, y2, rx, ry, rw, rh)``: 시작점 ``(x1, y1)``\ 으로부터 충돌 지점까지의 직선 거리 반환
* ``line_rect_dist_squared(...)``: 거리의 제곱 반환 (루트 연산이 없어 성능이 가장 빠름)
