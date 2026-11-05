시작하기
========

설치
----

``pgzhelper_rw`` 는 Python 3.7 이상 및 Pygame Zero 1.2 이상을 지원합니다.

.. code-block:: bash

    pip install pgzhelper_rw

기본 구조
---------

Pygame Zero 코드에서 ``pgzhelper`` 를 import하면 내장 ``Actor`` 클래스가 자동으로 확장된 기능들로 교체됩니다.

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

화면 제어
---------

전체 화면 모드와 창 모드를 간편하게 전환하거나 마우스 커서를 숨길 수 있습니다.

.. code-block:: python

    from pgzhelper import toggle_fullscreen, hide_mouse, show_mouse

    # 전체 화면 토글
    toggle_fullscreen()

    # 마우스 커서 숨기기
    hide_mouse()
