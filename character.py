import pygame
from pygame.locals import *


class Character:
    def __init__(self, image_path, pos):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # 이미지 축소
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move_left(self):
        self.rect.move_ip(-5, 0)

    def move_right(self):
        self.rect.move_ip(5, 0)

    def move_up(self):
        self.rect.move_ip(0, -5)

    def move_down(self):
        self.rect.move_ip(0, 5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Beginner(Character):
    def __init__(self, image_path, pos):
        super().__init__(image_path, pos)
        self.attack_power = 10
        self.defense_power = 5

    def attack(self, target):
        damage = self.attack_power - target.defense_power
        target.health -= damage

    def defend(self):
        self.defense_power += 2

    def draw(self, surface):
        super().draw(surface)
        # 캐릭터 위에 공격력과 방어력을 나타내는 문자열을 출력
        # font = pygame.font.SysFont(None, 30)
        # text = f"ATK: {self.attack_power} / DEF: {self.defense_power}"
        # text_surface = font.render(text, True, (255, 255, 255))
        # text_rect = text_surface.get_rect(center=self.rect.center)
        # surface.blit(text_surface, text_rect)
