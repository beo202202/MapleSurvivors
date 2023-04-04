import pygame
from pygame.locals import *

# character.py


class Character(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, screen):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # 이미지 축소
        self.rect = self.image.get_rect()
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

    # def hit(self, physical_att):
    #     self.hp -= physical_att
    #     # self.hp -= max(physical_att - self.physical_def, 1)
    #     if self.hp <= 0:
    #         # 게임 종료 또는 리스타트 등의 처리
    #         pass


class Beginner(Character):
    def __init__(self, image_path, pos, screen):
        super().__init__(image_path, pos, screen)
        # 나중에 주사위 굴리는 것도 넣기 ㅋ.ㅋ _str, _dex, _int, _luk 넣기
        self.lv = 1
        self.hp = 60
        self.max_hp = 50
        self.mp = 20
        self.max_mp = 20
        self.physical_att = 15
        self.magic_att = 7
        self.physical_def = 5
        self.magic_def = 2

    def update_status(self):
        self.hp = self.max_hp + 10 * self.lv
        self.mp = self.max_mp + 5 * self.lv
        self.physical_att = 10 + 5 * self.lv
        self.magic_att = 5 + 2 * self.lv

    def level_up(self):
        if self.exp >= self.max_exp:
            self.lv += 1
            self.exp = 0
            self.max_exp = self.lv * 5
            self.hp += 10
            self.max_hp += 10
            self.mp += 5
            self.max_mp += 5
            self.physical_att += 2
            self.magic_att += 1
            self.physical_def += 1
            self.magic_def += 1
            print(f"Level up! {self.name} is now level {self.lv}!")

            self.update_status()
            # 레벨업 이후에 추가적인 처리를 할 수 있음

    # def attack(self, target):
    #     damage = self.physical_att - target.physical_def
    #     target.health -= damage

    # def defend(self):
    #     self.defense_power += 2

    def draw(self, surface):
        super().draw(surface)
        # 캐릭터 위에 공격력과 방어력을 나타내는 문자열을 출력
        font = pygame.font.SysFont(None, 30)
        text = f"HP: {self.hp} / ATK: {self.physical_att} / DEF: {self.physical_def}"
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
