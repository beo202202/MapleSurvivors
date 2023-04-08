# skill.py
import pygame


class Skill():
    def __init__(self, duration, cooldown):
        self.duration = duration
        self.cooldown = cooldown
        self.start_time = None
        self.cooldown_time = 0

    def use(self, pos, player_rect, screen):
        self.start_time = pygame.time.get_ticks()
        self.pos = pygame.math.Vector2(player_rect.center)
        self.direction = pygame.math.Vector2(pos) - self.pos
        self.image_rect = self.image.get_rect(center=self.pos)

    def is_using(self):
        if self.start_time is not None:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            if elapsed_time >= self.duration:
                self.start_time = None
                return False
            return True

    def is_available(self):
        if self.cooldown_time == 0:
            return True
        elapsed_time = pygame.time.get_ticks() - self.cooldown_time
        if elapsed_time >= self.cooldown:
            self.cooldown_time = 0
            return True
        return False

    def start_cooldown(self):
        self.cooldown_time = pygame.time.get_ticks()

    def draw(self, screen):
        if self.is_using():
            self.image_rect.move_ip(self.direction.normalize() * 10)
            screen.blit(self.image, self.image_rect)

# 프로토


class Shell_Throwing(Skill):
    def __init__(self):
        super().__init__(1000, 500)
        self.image = pygame.image.load("imgs/snail_shell.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.radius = 25

    def use(self, pos, player_rect, screen):
        self.start_time = pygame.time.get_ticks()
        direction = pygame.math.Vector2(
            pos) - pygame.math.Vector2(player_rect.center)
        direction = direction.normalize()
        distance = 100  # 캐릭터에서 이동할 거리
        self.pos = pygame.math.Vector2(
            player_rect.center) + direction * distance
        self.direction = direction * distance  # 방향 벡터 계산

        self.image_rect = self.image.get_rect(center=self.pos)
        self.draw(screen)

    def draw(self, screen):
        if self.is_using():
            self.image_rect.move_ip(
                self.direction.normalize() * 10)  # 이동 거리를 10으로 조절
            screen.blit(self.image, self.image_rect)
