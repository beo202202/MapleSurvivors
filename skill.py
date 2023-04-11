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

    def draw(self, screen, FPS):
        if self.is_using():
            self.image_rect.move_ip(
                self.direction.normalize() * self.speed // FPS)
            screen.blit(self.image, self.image_rect)


class Shell_Throwing(Skill):
    def __init__(self):
        super().__init__(2000, 3000)  # duration: 2초, cooldown: 3초
        self.image = pygame.image.load("imgs/snail_shell.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.radius = 25

    def use(self, pos, player_rect, screen):
        if self.is_available():  # 스킬 사용 가능한 상태인지 체크
            self.start_time = pygame.time.get_ticks()
            self.direction = (
                pos - pygame.math.Vector2(player_rect.center)).normalize()
            distance = 100
            self.pos = pygame.math.Vector2(
                player_rect.center)  # + self.direction * distance
            self.image_rect = self.image.get_rect(center=self.pos)
            self.speed = distance // (self.duration // 1000)
            self.remaining_distance = distance
            self.start_cooldown()  # 스킬 사용 후 쿨타임 시작

    def is_using(self):
        if self.start_time is not None:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            if elapsed_time >= self.duration:
                self.start_time = None
                return False
            return True
        return False

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

    def draw(self, screen, FPS):
        if self.is_using():
            move_amount = self.speed / FPS
            self.pos += self.direction * move_amount
            self.image_rect.center = self.pos
            screen.blit(self.image, self.image_rect)
            self.remaining_distance -= move_amount
            if self.remaining_distance <= 0:
                self.start_time = None
