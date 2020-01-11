import os, pygame

clock = pygame.time.Clock()
pygame.init()
size = width, height = 600 ,300
screen = pygame.display.set_mode(size)
running = True
fps = 60


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Picture(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Picture.image
        self.speed = 200
        self.rect = self.image.get_rect()
        self.rect.x = -self.image.get_width()
        self.rect.y = 0

    def update(self, *args):
        self.rect.x += self.speed * clock.tick(fps) / 1000
        if self.rect.x + self.image.get_width() >= width:
            self.speed = 0



all_sprites = pygame.sprite.Group()
Picture(all_sprites)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
