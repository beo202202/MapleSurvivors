import pygame
import random

# monster.py


# monster.py

class Monster(pygame.sprite.Sprite):
    def __init__(self, image_path, map_size):
        super().__init__()
        self.speed = 1

        self.hp = 1
        self.max_hp = 1
        self.mp = 0
        self.max_mp = 0
        self.physical_att = 1
        self.magic_att = 0
        self.physical_def = 0
        self.magic_def = 0

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.radius = 25
        self.rect = self.image.get_rect()

        # 원형 몬스터의 위치를 맵 바깥쪽 좌표로 랜덤하게 생성
        if random.choice([True, False]):
            if random.choice([True, False]):
                self.rect.bottom = 0
            else:
                self.rect.top = map_size[1]
            self.rect.centerx = random.randint(0, map_size[0])
        else:
            if random.choice([True, False]):
                self.rect.right = 0
            else:
                self.rect.left = map_size[0]
            self.rect.centery = random.randint(0, map_size[1])

    def update(self, char_rect, map_rect, monsters):
        monster_rect = self.rect
        distance_x = char_rect.centerx - monster_rect.centerx
        distance_y = char_rect.centery - monster_rect.centery
        direction_x = 1 if distance_x > 0 else -1
        direction_y = 1 if distance_y > 0 else -1

        # 몬스터와 캐릭터의 거리에 따라 몬스터 이동 방향 결정
        self.rect.move_ip(direction_x * self.speed, direction_y * self.speed)

        # 위치 제한 추가
        monster_rect.clamp_ip(map_rect)

        # 몬스터가 맵 바깥쪽으로 나가지 않도록 처리
        if not map_rect.contains(monster_rect):
            if monster_rect.left < map_rect.left:
                monster_rect.left = map_rect.left
            elif monster_rect.right > map_rect.right:
                monster_rect.right = map_rect.right
            if monster_rect.top < map_rect.top:
                monster_rect.top = map_rect.top
            elif monster_rect.bottom > map_rect.bottom:
                monster_rect.bottom = map_rect.bottom

        # 몬스터끼리 충돌 검사
        for other in monsters:
            if other != self and self.rect.colliderect(other.rect):
                distance = self.rect.centerx - \
                    other.rect.centerx, self.rect.centery - other.rect.centery
                mag = (distance[0] ** 2 + distance[1] ** 2) ** 0.5
                overlap = (self.radius + other.radius) - mag
                direction = (distance[0] / mag, distance[1] / mag)
                self.rect.move_ip(
                    direction[0] * overlap, direction[1] * overlap)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Snail(Monster):
    def __init__(self, pos):
        super().__init__("img/snail.png", pos)
        self.speed = 1

        self.lv = 1
        self.hp = 15
        self.max_hp = 15
        self.mp = 0
        self.max_mp = 0
        self.physical_att = 2
        self.magic_att = 1
        self.physical_def = 0
        self.magic_def = 0

        self.exp = 3
        self.meso = 5


class BlueSnail(Monster):
    def __init__(self, pos):
        super().__init__("img/blue_snail.png", pos)
        self.speed = 1

        self.lv = 2
        self.hp = 20
        self.max_hp = 20
        self.mp = 0
        self.max_mp = 0
        self.physical_att = 3
        self.magic_att = 2
        self.physical_def = 0
        self.magic_def = 0

        self.exp = 4
        self.meso = 10


class RedSnail(Monster):
    def __init__(self, pos):
        super().__init__("img/red_snail.png", pos)
        self.speed = 1

        self.lv = 5
        self.hp = 50
        self.max_hp = 50
        self.mp = 0
        self.max_mp = 0
        self.physical_att = 15
        self.magic_att = 12
        self.physical_def = 3
        self.magic_def = 10

        self.exp = 8
        self.meso = 15
