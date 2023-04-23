import sys
import pygame
import random
from character import *
from monster import *
from map import *
from skill import *
from sound import SoundManager

WIN_WIDTH, WIN_HEIGHT = 1280, 1024
NUM_MONSTERS = 20
FPS = 60
# 스테이지 변수
stage = 0


# 사운드 매니저 초기화
sound_manager = SoundManager()
sound_manager.play_background_music()


def init_monsters(num_monsters, screen_size):
    monster_list = []
    # for i in range(num_monsters):
    # monster_type = random.choice([Snail, BlueSnail, Spore])
    # monster = monster_type(
    #     (random.randint(100, screen_size[0] - 100), random.randint(100, screen_size[1] - 100)), monster_list)
    # monster_list.append(monster)
    return monster_list


def init_game_objects(screen_size):
    maple_island = MapleIsland(screen_size)
    player = Beginner((screen_size[0] // 2, screen_size[1] // 2), screen)
    monster_list = init_monsters(NUM_MONSTERS, (WIN_WIDTH, WIN_HEIGHT))
    return maple_island, player, monster_list


# 게임 창 초기화
pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Maple Survivors")

# 타이틀 설정
pygame.display.set_caption("시간 표시 예제")

# 폰트 시스템 초기화
pygame.font.init()

# 폰트 초기화
font = pygame.font.Font(None, 36)

# 게임 맵, 캐릭터, 몬스터 초기화
maple_island, player, monster_list = init_game_objects((WIN_WIDTH, WIN_HEIGHT))
monster_list = init_monsters(NUM_MONSTERS, (WIN_WIDTH, WIN_HEIGHT))
# 스킬 초기화
shell_throwing = Shell_Throwing()

# 클럭 객체 생성
FPSCLOCK = pygame.time.Clock()


def restart_game():
    global maple_island, player, monster_list
    player = Beginner((WIN_WIDTH //
                      2, WIN_HEIGHT // 2), screen)
    monster_list = init_monsters(NUM_MONSTERS, (WIN_WIDTH, WIN_HEIGHT))
    maple_island = MapleIsland((WIN_WIDTH, WIN_HEIGHT))

# 스테이지를 업데이트하는 함수


def update_stage(current_time):
    global stage, monster_list
    stage_duration = 5 * 1000  # 스테이지의 지속 시간 (1분)

    # 스테이지 업데이트
    new_stage = current_time // stage_duration + 1

    if new_stage != stage:
        stage = new_stage

        # 스테이지별 몬스터 리스트 변경
        if stage == 1:
            num_new_monsters = 5
            new_monster_types = [Snail]
        elif stage == 2:
            num_new_monsters = 7
            new_monster_types = [Snail, BlueSnail]
        elif stage == 3:
            num_new_monsters = 5
            new_monster_types = [Snail, BlueSnail, Spore]
        elif stage == 4:
            num_new_monsters = 7
            new_monster_types = [BlueSnail, Spore, Stump]
        else:
            num_new_monsters = 5
            new_monster_types = [Orange_Mushroom]

        # 새로운 몬스터를 기존 몬스터 리스트에 추가합니다.
        for i in range(num_new_monsters):
            monster_type = random.choice(new_monster_types)
            monster = monster_type(
                (random.randint(100, WIN_WIDTH - 100), random.randint(100, WIN_HEIGHT - 100)), monster_list)
            monster_list.append(monster)


# 게임 루프
running = True
while running:

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP]:
        player.move_up()
    if keys[pygame.K_DOWN]:
        player.move_down()
    if keys[pygame.K_ESCAPE]:
        running = False

    # 게임 맵 업데이트
    maple_island.update(player.rect, screen.get_rect())

    # 게임 맵 그리기
    maple_island.draw(screen)

    # 몬스터 이동 및 충돌 검사
    for monster in monster_list:
        monster.hurt_timer = max(0, monster.hurt_timer - 1)  # 추가
        monster.update(player.rect, screen.get_rect(), monster_list)
        # 몬스터 그리기
        monster.draw(screen)

    # 캐릭터 그리기
    player.draw(screen)

    # 스킬 쿨다운 처리
    # shell_throwing.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # 마우스 오른쪽 버튼 눌림
                restart_game()

    # 현재 시간을 계산하고 이를 분과 초로 변환
    current_time = pygame.time.get_ticks()
    minutes = current_time // (60 * 1000)  # 밀리초를 분으로 변환
    seconds = (current_time % (60 * 1000)) // 1000  # 밀리초를 초로 변환

    # 스테이지 업데이트
    update_stage(current_time)

    # 스테이지 텍스트 생성
    stage_text = font.render(
        f"Stage {stage} FPS {int(FPSCLOCK.get_fps())}", True, (255, 255, 255))

    # 스테이지 텍스트 그리기
    screen.blit(stage_text, (10, 10))

    # 시간 텍스트 생성
    time_text = font.render(
        f"{minutes:02d}:{seconds:02d}", True, (255, 255, 255))

    # 시간 텍스트를 화면 상단 중앙에 그리기
    screen.blit(time_text, (WIN_WIDTH // 2 - time_text.get_width() //
                2, 10))

    # 자동으로 쿨타임마다 스킬 쓰기
    if shell_throwing.use(player.rect, player.direction):
        sound_manager.play_effect_sound("attack")

    # 스킬 그리기
    shell_throwing.draw(screen, FPS, monster_list)

    # 게임 화면 업데이트
    pygame.display.update()

    FPSCLOCK.tick(FPS)

# 게임 종료
pygame.quit()
