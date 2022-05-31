import pygame

WINDOW_SIZE = (600, 400)
pygame.init()
pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("snake game")
clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)
    pygame.display.update