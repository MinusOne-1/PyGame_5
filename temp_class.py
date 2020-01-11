import os, pygame, random

clock = pygame.time.Clock()
pygame.init()
size = width, height = 600, 95
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


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Car.image
        self.speed = 100
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.image.get_width() // 2
        self.rect.y = height // 2 - self.image.get_height() // 2

    def update(self, *args):
        if self.rect.x + self.image.get_width() >= width:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -self.speed
        elif self.rect.x <= 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed = -self.speed
        self.rect.x += self.speed * clock.tick(fps) / 1000


all_sprites = pygame.sprite.Group()
Car(all_sprites)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
