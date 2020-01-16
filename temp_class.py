import pygame

clock = pygame.time.Clock()
pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
running = True
fps = 60
#"гасим" курсор
pygame.mouse.set_visible(False)
#загружаем картинку курсора
MANUAL_CURSOR = pygame.image.load('data/arrow.png').convert_alpha()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if pygame.mouse.get_focused(): # если курсор в фокусе рисуем картинку
        screen.blit(MANUAL_CURSOR, (pygame.mouse.get_pos()))
    pygame.display.flip()
