import os, pygame, random

clock = pygame.time.Clock()
pygame.init()
size = width, height = 1280, 720
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


class Player(pygame.sprite.Sprite):
    image_pl = load_image("creature.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Player.image_pl
        self.rect = self.image.get_rect()
        self.rect.y = height // 2 - self.image.get_height() // 2
        self.rect.x = width // 2 - self.image.get_width() // 2

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == 275:
                self.rect.x += 10
            if args[0].key == 276:
                self.rect.x -= 10
            if args[0].key == 273:
                self.rect.y -= 10
            if args[0].key == 274:
                self.rect.y += 10


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom
            print(self.rect.width // 2)
            self.rect.x += self.rect.width // 2
            self.rect.y += self.rect.height // 2
            self.rect = self.image.get_rect()
            print(self.rect.width // 2)
            self.rect.x -= self.rect.width // 2
            self.rect.y -= self.rect.height // 2


all_sprites = pygame.sprite.Group()
Player(all_sprites)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
