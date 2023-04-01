from skill import Skill, AnimatedSkill
from skill import Skill
import pygame


class Skill:
    def __init__(self, image_path, duration, cooldown):
        self.image = pygame.image.load(image_path)
        self.duration = duration
        self.cooldown = cooldown
        self.start_time = None
        self.cooldown_time = 0

    def use(self, pos):
        self.start_time = pygame.time.get_ticks()
        self.pos = pos

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
            screen.blit(self.image, self.pos)


class SnailGuardSkill(AnimatedSkill):
    def __init__(self, image_path, radius, damage, duration, cooldown):
        super().__init__(image_path, duration, cooldown)
        self.radius = radius
        self.damage = damage
        self.skill_image_2 = pygame.image.load("img/throw_snail_2.gif")
        self.skill_image_2 = pygame.transform.scale(
            self.skill_image_2, (64, 64))
        self.skill_image_frames = self.animate_gif(
            self.skill_image, num_frames=10, frame_duration=100, loop=True)
        self.skill_image_2_frames = self.animate_gif(
            self.skill_image_2, num_frames=10, frame_duration=100, loop=True)

    def use(self, pos, monsters):
        for monster_rect, monster_image in monsters:
            if pygame.math.Vector2(monster_rect.center - pos).length() <= self.radius:
                monster_rect.move_ip(10, 0)
                # 몬스터에게 데미지를 입히는 코드 추가
                self.play_animation(self.skill_image_2_frames, 500)
                pygame.time.wait(500)
                self.play_animation(self.skill_image_frames, self.duration)
                break
            else:
                self.play_animation(self.skill_image_frames, self.duration)
