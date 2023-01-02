# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import math

WIDTH = 1000
HEIGHT = 1000
FPS = 300
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SPEED = 5
G = 0.5

#загружаем спрайты
SPRITES = [pygame.image.load('einstein.png')]

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spx = 0
        self.spy = 0
        self.mass = 1
        self.image = pygame.Surface((50, 49))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, WIDTH))
    def update(self):
        global SPEED, SPRITES, objects, G
        screen.blit(SPRITES[0], (self.rect.x, self.rect.y))
        for obj in objects:
            if not (obj.rect.x == self.rect.x and obj.rect.y == self.rect.y):
                x = self.rect.x
                y = self.rect.y
                x1 = obj.rect.x
                y1 = obj.rect.y
                self.spx += G * obj.mass * (x1 - x) / (((x1 - x) ** 2 + (y1 - y) ** 2) ** (3 / 2))
                self.spy += G * obj.mass * (y1 - y) / (((x1 - x) ** 2 + (y1 - y) ** 2) ** (3 / 2))
        self.rect.x += self.spx
        self.rect.y += self.spy
        if self.rect.x <= 10:
            self.spx = math.fabs(self.spx)
        if self.rect.x >= WIDTH:
            self.spx = -1 * math.fabs(self.spx)
        if self.rect.y <= 10:
            self.spy = math.fabs(self.spy)
        if self.rect.y >= HEIGHT:
            self.spy = -1 * math.fabs(self.spy)


        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += SPEED
        '''


all_sprites = pygame.sprite.Group()
objects = []

for i in range(3):
    new_player = Player()
    all_sprites.add(new_player)
    objects.append(new_player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()


pygame.quit()
