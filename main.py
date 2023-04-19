import sys
import pygame
import random
from character import *
from monster import *
from map import *
from skill import *

WIN_WIDTH, WIN_HEIGHT = 1280, 1024
NUM_MONSTERS = 10
FPS = 60

# 캐릭터와 몬스터가 30 fps로 줄었을 경우 느려짐 문제


def init_monsters(num_monsters, screen_size):
    monster_list = []
    for i in range(num_monsters):
        monster_type = random.choice([Snail, BlueSnail, RedSnail])
        monster = monster_type(
            (random.randint(100, screen_size[0] - 100), random.randint(100, screen_size[1] - 100)), monster_list)
        monster_list.append(monster)
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

    # visible_monster_rects = []  # 화면 안에 들어있는 몬스터들의 위치 정보 저장

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
            # if event.button == 1:  # 마우스 왼쪽 버튼 눌림
            #     # 마우스 클릭 위치로 스킬 사용
            #     shell_throwing.use(pygame.mouse.get_pos(),
            #                        player.rect, screen)
            if event.button == 3:  # 마우스 오른쪽 버튼 눌림
                restart_game()

    # 자동으로 쿨타임마다 스킬 쓰기
    shell_throwing.use(player.rect, player.direction)

    # 스킬 그리기
    shell_throwing.draw(screen, FPS, monster_list)

    # 게임 화면 업데이트
    pygame.display.update()

    FPSCLOCK.tick(FPS)

# 게임 종료
pygame.quit()
