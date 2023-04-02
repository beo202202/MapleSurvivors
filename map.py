import pygame


class Map:
    def __init__(self, image_path, size):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (size[0]*5, size[1]*5))
        self.rect = self.image.get_rect(center=(size[0] // 2, size[1] // 2))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, player_rect, screen_rect):
        self.rect.center = player_rect.center
        # 게임 화면 범위 내에서만 맵 이미지가 보이도록 처리합니다.
        self.rect.clamp_ip(screen_rect)

        # 캐릭터가 맵 밖으로 나가지 않도록 처리합니다.
        if not self.rect.contains(player_rect):
            player_rect.clamp_ip(self.rect)


class MapleIsland(Map):
    def __init__(self, size):
        super().__init__("img/maple_island.png", size)
        self.offset = (0, 0)

    def update(self, player_rect, screen_size):
        # 맵 이미지와 화면의 상대 위치 계산
        x = -(player_rect.centerx - screen_size[0]//2) * 4
        y = -(player_rect.centery - screen_size[1]//2) * 4
        self.offset = (x, y)
        # 화면 범위 내에서만 맵 이미지가 보이도록 처리
        self.rect = self.image.get_rect(
            center=(screen_size[0]//2 + x//5, screen_size[1]//2 + y//5))
        self.rect.clamp_ip(pygame.Rect((0, 0, screen_size[0], screen_size[1])))

    def draw(self, screen):
        screen.blit(self.image, self.offset)
