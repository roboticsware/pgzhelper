pgzhelper: Pygame Zero를 위한 필수 도우미 라이브러리
====================================================

**pgzhelper (pgzhelper_rw)**\ 는 `Pygame Zero <https://pygame-zero.readthedocs.io/>`_\ 의 기능을 확장하여 스크래치(Scratch) 스타일의 직관적인 액터 제어와 게임 개발에 필수적인 고급 충돌 감지, 애니메이션, 이미지 변형 기능을 제공하는 라이브러리입니다.

.. tip::
   🌐 **English Version**: You can find the English version of this documentation in the `docs/en/` directory.

주요 특징
---------

* **Actor 확장 기능**:

  * **스크래치 스타일 이동/회전**: ``move_forward()``, ``point_towards()``, ``distance_to()`` 등
  * **스프라이트 애니메이션**: 여러 이미지를 등록하고 ``fps`` 지정으로 부드러운 애니메이션 실행
  * **이미지 조작 & 효과**: 크기 조절(``scale``), 좌우/상하 반전(``flip_x``, ``flip_y``), 실시간 색조 변경(``add_hue()``)
  * **말풍선 & 붓 그리기**: ``say()`` 말풍선 대사 출력 및 이동 궤적을 그리는 ``brush_*`` 기능

* **강력한 충돌 감지 (Collision Detection)**:

  * 점(Point), 선(Line), 원(Circle), AABB 사각형(Rect), 회전 사각형(OBB) 간의 완벽한 충돌 판정
  * 여러 대상과의 충돌을 고속으로 검사하는 복수형 함수 (예: ``circle_points``, ``obb_lines`` 등)
  * 최근접 충돌 지점 좌표 및 거리 계산 지원 (예: ``line_circle_XY``, ``line_rect_dist``)

* **편의 유틸리티**:

  * 전체화면 전환 (``toggle_fullscreen``), 마우스 커서 숨김/표시 (``hide_mouse``, ``show_mouse``)

설치 방법
---------

pip를 통해 간편하게 설치할 수 있습니다:

.. code-block:: bash

    pip install pgzhelper_rw

빠른 시작 예제
--------------

.. code-block:: python

    import pgzrun
    from pgzhelper import *

    WIDTH = 800
    HEIGHT = 600

    alien = Actor('alien')
    alien.topleft = 100, 100

    def update():
        # 마우스 위치를 향해 부드럽게 회전하고 이동
        alien.point_towards(pygame.mouse.get_pos())
        alien.move_forward(3)

    def draw():
        screen.clear()
        alien.draw()

    pgzrun.go()

목차
----

.. toctree::
   :maxdepth: 2
   :caption: 사용자 가이드

   gettingstarted
   actor
   collision
   api

.. toctree::
   :maxdepth: 1
   :caption: 프로젝트 정보

   contributing
   license
