import pygame
from pygame.locals import *

# character.py


class Character(pygame.sprite.Sprite):
    def __init__(self, pos, screen):
        self.image_path = "imgs/dodo.png"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # 이미지 축소
        self.rect = self.image.get_rect()
        self.direction = "left"
        self.rect.center = pos
        self.screen = screen
        self.speed = 2

        self.lv = 1
        self.hp = 50
        self.max_hp = 1
        self.mp = 0
        self.max_mp = 0
        self.physical_att = 1
        self.magic_att = 0
        self.physical_def = 0
        self.magic_def = 0

        self.skill_cool_time = 0

    def move_left(self):
        new_rect = self.rect.move(-self.speed, 0)
        if self.check_collision(new_rect):
            self.rect = new_rect

    def move_right(self):
        new_rect = self.rect.move(self.speed, 0)
        if self.check_collision(new_rect):
            self.rect = new_rect

    def move_up(self):
        new_rect = self.rect.move(0, -self.speed)
        if self.check_collision(new_rect):
            self.rect = new_rect

    def move_down(self):
        new_rect = self.rect.move(0, self.speed)
        if self.check_collision(new_rect):
            self.rect = new_rect

    def draw(self, screen):
        # 마우스 위치와 캐릭터 위치 비교
        if pygame.mouse.get_pos()[0] < self.rect.centerx:
            image = self.image
            self.direction = "left"
        else:
            image = pygame.transform.flip(self.image, True, False)
            self.direction = "right"

        # 이미지 그리기
        screen.blit(image, self.rect)

        # 캐릭터 밑에 체력, 공격력과 방어력을 나타내는 문자열을 출력
        font = pygame.font.SysFont(None, 30)

        # HP 텍스트 출력 (빨간색)
        hp_text = f"HP: {self.hp}"
        hp_text_surface = font.render(hp_text, True, (255, 0, 0))
        hp_text_rect = hp_text_surface.get_rect(
            center=(self.rect.centerx, self.rect.bottom + 10))
        screen.blit(hp_text_surface, hp_text_rect)

        # MP 텍스트 출력 (파란색)
        mp_text = f"MP: {self.mp}"
        mp_text_surface = font.render(mp_text, True, (0, 0, 255))
        mp_text_rect = mp_text_surface.get_rect(
            center=(self.rect.centerx, self.rect.bottom + 30))
        screen.blit(mp_text_surface, mp_text_rect)

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
    def __init__(self, pos, screen):
        super().__init__(pos, screen)
        self.image_path = "imgs/beginner.png"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # 이미지 축소
        self.name = "초보자"
        self.lv = 1
        self.hp = 60
        self.max_hp = 50
        self.mp = 20
        self.max_mp = 20
        self.physical_att = 15
        self.magic_att = 7
        self.physical_def = 5
        self.magic_def = 2
        self.exp = 0
        self.max_exp = 50

    def update_status(self):
        self.max_hp = self.max_hp + 2 * self.max_hp
        self.hp = self.max_hp
        self.max_mp = self.max_mp + 2 * self.max_mp
        self.mp = self.max_mp
        self.physical_att = 10 + 2 * self.physical_att
        self.magic_att = 5 + 2 * self.magic_att

    def level_up(self):
        if self.exp >= self.max_exp:
            self.lv += 1

            # 경험 남는 거 이전하기
            self.exp -= self.max_exp
            self.max_exp += self.max_exp * 2

            self.max_hp += self.max_hp * 2
            self.hp = self.max_hp

            self.max_mp += self.max_mp * 2
            self.mp = self.max_mp

            self.physical_att += 5 + 2 * self.physical_att
            self.physical_def += 3 + 1 * self.physical_def

            self.magic_att += 5 + 2 * self.magic_att
            self.magic_def += 1 + 1 * self.magic_def

            print(f"Level up! {self.name} is now level {self.lv}!")

            self.update_status()
            # 레벨업 이후에 추가적인 처리를 할 수 있음
