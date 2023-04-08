import pygame
import random
from character import Beginner
from monster import Snail, BlueSnail, RedSnail
from map import Map, MapleIsland

WIN_WIDTH, WIN_HEIGHT = 1280, 1024
NUM_MONSTERS = 50


def init_monsters(num_monsters, screen_size):
    monster_list = []
    for i in range(num_monsters):
        monster_type = random.choice([Snail, BlueSnail, RedSnail])
        monster = monster_type(
            (random.randint(100, screen_size[0] - 100), random.randint(100, screen_size[1] - 100)))
        monster_list.append(monster)
    return monster_list


def init_game_objects(screen_size):
    maple_island = MapleIsland(screen_size)
    player = Beginner(
        "img/dodo.png", (screen_size[0] // 2, screen_size[1] // 2), screen)
    return maple_island, player


# 게임 창 초기화
pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Maple Survivors")

# 게임 맵, 캐릭터, 몬스터 초기화
maple_island, player = init_game_objects((WIN_WIDTH, WIN_HEIGHT))
monster_list = init_monsters(NUM_MONSTERS, (WIN_WIDTH, WIN_HEIGHT))


def restart_game():
    global maple_island, player, monster_list
    player = Beginner("img/dodo.png", (WIN_WIDTH //
                      2, WIN_HEIGHT // 2), screen)
    monster_list = init_monsters(NUM_MONSTERS, (WIN_WIDTH, WIN_HEIGHT))
    maple_island = MapleIsland((WIN_WIDTH, WIN_HEIGHT))


# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # 마우스 오른쪽 버튼 눌림
                restart_game()

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
        monster.update(player.rect, screen.get_rect(), monster_list)
        monster.draw(screen)

    # 캐릭터 그리기
    player.draw(screen)

    # 게임 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
