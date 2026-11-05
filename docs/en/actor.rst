액터 확장 기능 (Actor Guide)
=============================

``pgzhelper`` 의 ``Actor`` 는 Pygame Zero의 기본 액터에 다양한 게임 개발 편의 기능을 추가합니다.

이동 및 회전 (Scratch 스타일)
-----------------------------

스크래치 블록처럼 직관적으로 액터를 이동하고 방향을 회전할 수 있습니다.

.. code-block:: python

    # 현재 각도(angle) 기준으로 직진 이동
    actor.move_forward(5)

    # 뒤로 이동
    actor.move_back(5)

    # 좌/우 게걸음 이동 (스트레이프)
    actor.move_left(5)
    actor.move_right(5)

    # 특정 각도 방향으로 이동
    actor.move_in_direction(5)

    # 다른 액터 또는 좌표(x, y)를 향해 바라보기 (회전)
    actor.point_towards(target_actor)
    actor.point_towardsXY(400, 300)

    # 대상과의 거리 및 각도 계산
    dist = actor.distance_to(target_actor)
    deg = actor.direction_to(target_actor)

    # 대상을 향해 일정 거리만큼 이동 (도착 시 멈춤 옵션)
    actor.move_towards(target_actor, dist=3, stop_on_target=True)

이미지 변형 & 색조 조절
-----------------------

크기 변경, 좌우/상하 반전, 그리고 실시간 색조 회전을 지원합니다.

.. code-block:: python

    # 1. 크기 조절 (배율)
    actor.scale = 1.5

    # 2. 좌우 및 상하 반전
    actor.flip_x = True   # 좌우 반전
    actor.flip_y = False  # 상하 반전

    # 3. 색조 (Hue) 변경
    # 총알 피격 등 이벤트마다 색조를 30도씩 누적 회전
    actor.add_hue(30)

    # 특정 색조 각도로 직접 지정 (0~360)
    actor.hue = 180

.. note::
   색조 변환은 고속 NumPy 가속 및 내부 서피스 캐싱이 적용되어 프레임 저하 없이 부드럽게 작동합니다.

스프라이트 애니메이션
---------------------

여러 프레임의 이미지를 등록하여 자동으로 순환하는 애니메이션을 구현할 수 있습니다.

.. code-block:: python

    # 이미지 목록 등록
    actor.images = ['walk_0', 'walk_1', 'walk_2', 'walk_3']
    actor.fps = 10  # 초당 10프레임 속도

    def update():
        # update() 내에서 프레임을 자동으로 전진시킵니다
        actor.animate()

말풍선 (Speech Bubble)
----------------------

액터 머리 위에 말풍선 텍스트를 렌더링할 수 있습니다.

.. code-block:: python

    # 텍스트와 말풍선 크기, 색상 지정
    actor.say("안녕하세요!", width=150, height=40, fgcolor='black', bgcolor='white')

    # 말풍선 지우기
    actor.say("")

붓 그리기 (Brush Trail)
-----------------------

액터가 움직인 궤적을 화면에 선으로 남길 수 있습니다.

.. code-block:: python

    # 1. 붓 초기화 (화면 크기, 두께, 색상)
    actor.brush_init((800, 600), thick=3, color='yellow')

    # 2. 그리기 시작
    actor.brush_start()

    # 3. 매 프레임 draw()에서 화면에 붓 레이어 렌더링
    def draw():
        screen.clear()
        actor.brush_draw()  # 궤적 그리기
        actor.draw()

    # 4. 그리기 중지 및 초기화
    actor.brush_stop()
    actor.brush_clear()
