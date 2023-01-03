# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import math

WIDTH = 1000
HEIGHT = 1000
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SPEED = 5
G = 0.001

#загружаем спрайты
SPRITES = [pygame.image.load('einstein.png')]

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.spx = 0
        self.spy = 0
        self.mass = 1
        self.image = pygame.Surface((50, 49))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def update(self):
        global SPRITES
        screen.blit(SPRITES[0], (self.rect.x, self.rect.y))
        self.rect.center = (self.rect.center[0] + self.spx, self.rect.center[1] + self.spy)


all_sprites = pygame.sprite.Group()
objects = []

def CREATE_OBJ(pos):
    global Player, all_sprites, objects
    new_player = Player(pos)
    all_sprites.add(new_player)
    objects.append(new_player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    for this in objects:
        x = this.rect.center[0]
        y = this.rect.center[1]
        for other in objects:
            x1 = other.rect.center[0]
            y1 = other.rect.center[1]
            if this.rect.center != other.rect.center:
                this.spx += G * (x1 - x)
                this.spy += G * (y1 - y)
        this.rect.center = (x + this.spx, y + this.spy)
    

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
                CREATE_OBJ(event.pos)
    # Обновление
    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
