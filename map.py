import pygame


class Map:
    def __init__(self, image_path, size):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(size[0] // 2, size[1] // 2))
        self.width = self.rect.width
        self.height = self.rect.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, player_rect, screen_rect):
        self.rect.center = player_rect.center
        self.rect.clamp_ip(screen_rect)

        if not self.rect.contains(player_rect):
            player_rect.clamp_ip(self.rect)

    def get_size(self):
        return self.width, self.height


class MapleIsland(Map):
    def __init__(self, size):
        super().__init__("imgs/maple_island.png", size)
        self.offset = (0, 0)

    # def update(self, player_rect, screen_size):
    #     # 캐릭터와 맵의 상대 위치 계산
    #     x = -(player_rect.centerx - screen_size[0] // 2) * 4
    #     y = -(player_rect.centery - screen_size[1] // 2) * 4

    #     # 캐릭터가 화면 중앙에 위치할 때만 맵을 이동시킴
    #     if abs(x) < screen_size[0] // 4:
    #         self.offset = (x, self.offset[1])
    #     if abs(y) < screen_size[1] // 4:
    #         self.offset = (self.offset[0], y)

    #     # 화면 범위 내에서만 맵 이미지가 보이도록 처리
    #     self.rect = self.image.get_rect(
    #         center=(screen_size[0]//2 + self.offset[0]//5, screen_size[1]//2 + self.offset[1]//5))
    #     self.rect.clamp_ip(pygame.Rect((0, 0, screen_size[0], screen_size[1])))
