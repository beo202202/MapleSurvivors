import pygame
from pygame.locals import *


class Character(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, screen):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # 이미지 축소
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.screen = screen

    def move_left(self):
        new_rect = self.rect.move(-1, 0)
        if self.check_collision(new_rect):
            self.rect = new_rect

    def move_right(self):
        new_rect = self.rect.move(1, 0)
        if self.check_collision(new_rect):
            self.rect = new_rect

    def move_up(self):
        new_rect = self.rect.move(0, -1)
        if self.check_collision(new_rect):
            self.rect = new_rect

    def move_down(self):
        new_rect = self.rect.move(0, 1)
        if self.check_collision(new_rect):
            self.rect = new_rect

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, map_rect):
        # 캐릭터가 맵 밖으로 나가지 않도록 처리합니다.
        self.rect.clamp_ip(map_rect)

    def check_collision(self, rect):
        if rect.left < 0 or rect.right > self.screen.get_width():
            return False
        if rect.top < 0 or rect.bottom > self.screen.get_height():
            return False
        return True


class Beginner(Character):
    def __init__(self, image_path, pos, screen):
        super().__init__(image_path, pos, screen)
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
