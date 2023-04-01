import pygame


class Map:
    def __init__(self, image_path, size):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(size[0] // 2, size[1] // 2))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class MapleIsland(Map):
    def __init__(self, size):
        super().__init__("img/maple_island.png", size)
        # 더 추가할 속성이 있다면 여기에 추가합니다.
