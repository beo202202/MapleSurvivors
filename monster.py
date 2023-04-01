import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, image_path, pos):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # 이미지 크기 조정
        self.rect = self.image.get_rect(center=pos)

    def update(self, char_rect, win_rect):
        monster_rect = self.rect
        distance = char_rect.centerx - monster_rect.centerx
        direction = 1 if distance > 0 else -1

        # 몬스터와 캐릭터의 거리에 따라 몬스터 이동 방향 결정
        self.rect.move_ip(direction * self.speed, 0)

        # if abs(distance) < 300:
        #    monster_rect.move_ip(direction * self.speed, 0)

        # 위치 제한 추가
        monster_rect.clamp_ip(win_rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Snail(Monster):
    def __init__(self, pos):
        super().__init__("img/snail.png", pos)
        self.speed = 0.1
        # 더 추가할 속성이 있다면 여기에 추가합니다.


class BlueSnail(Monster):
    def __init__(self, pos):
        super().__init__("img/blue_snail.png", pos)
        self.speed = 0.1
        # 더 추가할 속성이 있다면 여기에 추가합니다.


class RedSnail(Monster):
    def __init__(self, pos):
        super().__init__("img/red_snail.png", pos)
        self.speed = 0.1
        # 더 추가할 속성이 있다면 여기에 추가합니다.
