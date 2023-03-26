import pygame

# 초기화
pygame.init()

# size = [800, 600]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("연습")

# 음악 파일 로드 및 10초부터 재생
pygame.mixer.music.load("./sounds/구버전 메인화면 - Title.mp3")
pygame.mixer.music.play(-1)

while True:
    pygame.display.update()

# 종료
# pygame.quit()
