import pygame

W = 800
H = 600
SILVER = (192, 192, 192)
BLUE = (0, 0, 100)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption("Задание на урок")
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 74, True, False)
# screen = pygame.Surface((W - font.get_height(), font.get_height()))
font_rect = screen.get_rect(center=(W // 2, H - font.get_height()))
font2 = pygame.font.SysFont('Arial', 14, True, False)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    screen.fill(BLUE)
    pygame.display.update()
