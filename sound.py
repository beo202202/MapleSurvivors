import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.background_music = pygame.mixer.music.load(
            "sounds/메이플 아일랜드 - Maple_Leaf.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
        self.effect_sounds = {
            'attack': pygame.mixer.Sound('sounds/Maplestory-007.wav')
            # '피격': pygame.mixer.Sound('sounds/Maplestory-008.wav')
        }

    def play_background_music(self):
        pygame.mixer.music.play(-1)

    def stop_background_music(self):
        pygame.mixer.music.stop()

    def play_effect_sound(self, sound_name):
        if sound_name in self.effect_sounds:
            self.effect_sounds[sound_name].set_volume(0.5)
            self.effect_sounds[sound_name].play()
