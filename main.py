import pygame
import random
import itertools
from pygame.locals import *

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

# 캐릭터 속성 초기화
# Create a timer event that will reset the character's transparency level after 1 second
# invincible_timer = pygame.time.set_timer(pygame.USEREVENT, 1000)
# 무적 시간
invincible_time = 1
char_health = 100
char_invincible = False
invincibility_cooldown = 500  # 1 second in milliseconds

# 몬스터 초기화
monster_images = [
    pygame.image.load("img/snail.png"),
    pygame.image.load("img/blue_snail.png"),
    pygame.image.load("img/red_snail.png")
]
monster_list = []
for i in range(10):
    monster_image = monster_images[random.randint(0, 2)]
    monster_rect = monster_image.get_rect()
    monster_rect.center = (random.randint(
        100, win_width-100), random.randint(100, win_height-100))
    monster_list.append((monster_rect, monster_image))


# 메소 초기화
meso_images = [
    pygame.image.load("img/0-49meso.png"),
    pygame.image.load("img/50-99meso.png"),
    pygame.image.load("img/100-999meso.png"),
    pygame.image.load("img/1000-meso.png")
]
meso_list = []

# 스킬 GIF 초기화
skill_image = pygame.image.load("img/throw_snail.gif")
skill_image_2 = pygame.image.load("img/throw_snail_2.gif")

# Skill position and rotation initialization
skill_pos = char_rect.center
skill_rotation_speed = 5
skill_rotation_radius = 50
angle = 0


def animate_gif(image, num_frames, frame_duration, loop=True):
    frames = []
    for i in range(num_frames):
        frame = pygame.Surface(
            (image.get_width(), image.get_height() // num_frames), SRCALPHA, 32)
        frame.blit(image, (0, -i * image.get_height() // num_frames))
        frames.append(frame)

    if loop:
        return itertools.cycle(frames)
    else:
        return frames


def skill():
    pass


skill_image_frames = animate_gif(
    skill_image, num_frames=10, frame_duration=100)
skill_image_2_frames = animate_gif(
    skill_image_2, num_frames=10, frame_duration=100)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            char_invincible = False
            # char_image.set_alpha(255)

    # 키보드 입력 처리, ESC 추가해야함.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        char_rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        char_rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        char_rect.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        char_rect.move_ip(0, 5)
    if keys[pygame.K_ESCAPE]:
        running = False

    # 게임 맵 그리기
    screen.blit(bg_image, bg_rect)

    # 몬스터 그리기
    for monster_rect, monster_image in monster_list:
        screen.blit(monster_image, monster_rect)

    # 메소 그리기
    for meso_rect, meso_image in meso_list:
        screen.blit(meso_image, meso_rect)

    # 캐릭터 그리기
    if char_invincible:
        char_image.set_alpha(128)
    else:
        char_image.set_alpha(255)
    screen.blit(char_image, char_rect)

    # 충돌 검사
    for monster_rect, monster_image in monster_list:
        # 캐릭터와 몬스터 충돌
        if char_rect.colliderect(monster_rect) and not char_invincible:
            char_health -= 10
            char_invincible = True
            char_image.set_alpha(128)
            pygame.time.set_timer(pygame.USEREVENT, invincibility_cooldown)

        # 스킬과 몬스터 충돌
        # if skill_rect.colliderect(monster_rec)
            # 메소 드랍 확률 설정
            # meso_drop_chance = random.randint(1, 100)
            # if meso_drop_chance >= 50:
            #     meso_value = random.randint(1, 10000)
            #     if meso_value < 50:
            #         meso_image = meso_images[0]
            #     elif meso_value < 100:
            #         meso_image = meso_images[1]
            #     elif meso_value < 1000:
            #         meso_image = meso_images[2]
            #     else:
            #         meso_image = meso_images[3]
            #     meso_rect = meso_image.get_rect()
            #     meso_rect.center = (random.randint(
            #         100, win_width-100), random.randint(100, win_height-100))
            #     meso_list.append((meso_rect, meso_image))

            # 패배한 몬스터 제거하기
            # monster_list.remove((monster_rect, monster_image))

    # 스킬 함수 중 끌어와야함.
    # Rotate the skill_image around the character
    distance = 50
    angle += 0.1
    offset = pygame.math.Vector2(0, -distance).rotate(-angle)
    skill_rect = skill_image.get_rect(center=char_rect.center + offset)
    screen.blit(skill_image, skill_rect)

    # 게임 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
