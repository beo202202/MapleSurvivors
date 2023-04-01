import pygame
import random

# 게임 창 초기화
pygame.init()
win_width, win_height = 800, 600
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Maple Survivors")

# 게임 맵 초기화
bg_image = pygame.image.load("img/maple_island.png")
bg_image = pygame.transform.scale(bg_image, (win_width, win_height))
bg_rect = bg_image.get_rect()
bg_rect.center = (win_width // 2, win_height // 2)

# 캐릭터 초기화
char_image = pygame.image.load("img/dodo.png")
char_image = pygame.transform.scale(char_image, (64, 64))
char_rect = char_image.get_rect()
char_rect.center = (win_width // 2, win_height // 2)

# 몬스터 초기화
monster_images = [
    pygame.image.load("img/snail.png"),
    pygame.image.load("img/blue_snail.png"),
    pygame.image.load("img/red_snail.png")
]
monster_images = [pygame.transform.scale(
    img, (64, 64)) for img in monster_images]
monster_list = []
for i in range(10):
    monster_rect = monster_images[random.randint(0, 2)].get_rect()
    monster_rect.center = (random.randint(
        100, win_width-100), random.randint(100, win_height-100))
    monster_list.append(monster_rect)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 맵 그리기
    screen.blit(bg_image, bg_rect)

    # 몬스터 그리기
    for monster_rect, monster_image in zip(monster_list, monster_images):
        screen.blit(monster_image, monster_rect)

    # 캐릭터 그리기
    screen.blit(char_image, char_rect)

    # 게임 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
