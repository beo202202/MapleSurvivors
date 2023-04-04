import pygame
import random
from character import Beginner
from monster import Snail, BlueSnail, RedSnail
from map import Map, MapleIsland

# 게임 창 초기화
pygame.init()
win_width, win_height = 1280, 1024
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Maple Survivors")

# 게임 맵 초기화
maple_island = MapleIsland((win_width, win_height))

# 캐릭터 초기화
player = Beginner("img/dodo.png", (win_width // 2, win_height // 2), screen)

# 몬스터 초기화
monster_list = []
for i in range(20):
    monster_type = random.choice([Snail, BlueSnail, RedSnail])
    monster = monster_type(
        (random.randint(100, win_width - 100), random.randint(100, win_height - 100)))
    monster_list.append(monster)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    # monster_group.update(player.rect, screen.get_rect())

    # 일부 겹치게 해서 버그가 없게 만들기
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
