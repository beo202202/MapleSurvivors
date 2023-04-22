# monster.py
import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, image_path, map_size, monster_list):
        super().__init__()
        self.name = "monster"
        self.speed = 1
        self.hurt_timer = 0  # 적중했을 때 빨간색으로 깜빡이는 시간
        self.monster_list = monster_list
        self.direction = random.choice(["left", "right", "up", "down"])

        self.lv = 1
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
        self.original_image = self.image.copy()  # 새로운 변수 추가
        self.radius = 25
        self.rect = self.image.get_rect()
       # 폰트 미리 로드
        self.font = pygame.font.SysFont(None, 30)

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

        # 0 디바이드 오류? + 모여서 멈추면 앞으로 안옴.
        # 몬스터끼리 충돌 검사
        # for other in monsters:
        #     if other != self and self.rect.colliderect(other.rect):
        #         distance = self.rect.centerx - \
        #             other.rect.centerx, self.rect.centery - other.rect.centery
        #         mag = (distance[0] ** 2 + distance[1] ** 2) ** 0.5
        #         overlap = (self.radius + other.radius) - mag
        #         direction = (distance[0] / mag, distance[1] / mag)
        #         self.rect.move_ip(
        #             direction[0] * overlap, direction[1] * overlap)

        # 플레이어와의 충돌 검사
        if self.rect.colliderect(char_rect):
            # 충돌 시 플레이어의 체력 감소
            # Character.hp -= 10
            # Character.hit(20)
            pass

        # 몬스터의 중심점(center) 값을 갱신합니다.
        self.center = self.rect.center

    def draw(self, screen):
        if self.hurt_timer > 0:
            self.image.fill((255, 0, 0, 255))
            self.hurt_timer -= 1
            if self.hurt_timer == 0:
                self.image = self.original_image.copy()  # 복원하기
            # print(f'{self.name=}, {self.hurt_timer=}')
        screen.blit(self.image, self.rect)

        # # 현재 몬스터의 위치 정보가 화면 안에 들어있는지 확인 (랙 안걸리는...)
        # if self.rect.collidelist(visible_monster_rects) != -1:
        #     screen.blit(self.image, self.rect)

        # 몬스터 밑에 체력, 공격력과 방어력을 나타내는 문자열을 출력
        font = pygame.font.SysFont(None, 30)
        hp_text = f"HP: {self.hp}"
        hp_text_surface = font.render(hp_text, True, (255, 0, 0))
        hp_text_rect = hp_text_surface.get_rect(
            center=(self.rect.centerx, self.rect.bottom + 10))
        screen.blit(hp_text_surface, hp_text_rect)

        att_text = f"ATK: {self.physical_att}"
        att_text_surface = font.render(att_text, True, (0, 0, 255))
        att_text_rect = att_text_surface.get_rect(
            center=(self.rect.centerx, self.rect.bottom + 30))
        screen.blit(att_text_surface, att_text_rect)

        def_text = f"DEF: {self.physical_def}"
        def_text_surface = font.render(def_text, True, (0, 255, 0))
        def_text_rect = def_text_surface.get_rect(
            center=(self.rect.centerx, self.rect.bottom + 50))
        screen.blit(def_text_surface, def_text_rect)

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill(self.monster_list)  # 킬이 됨.

    def kill(self, monster_list):
        super().kill()  # 스프라이트 그룹에서 제거
        monster_list.remove(self)  # monster_list에서도 제거


class Snail(Monster):
    def __init__(self, pos, monster_list):
        super().__init__("imgs/snail.png", pos, monster_list)
        self.name = "달팽이"
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
    def __init__(self, pos, monster_list):
        super().__init__("imgs/blue_snail.png", pos, monster_list)
        self.name = "파란 달팽이"
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
    def __init__(self, pos, monster_list):
        super().__init__("imgs/red_snail.png", pos, monster_list)
        self.name = "빨간 달팽이"
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
