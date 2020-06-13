import pygame
from road_setting import *
import time


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(Player_im)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - 150
        self.power = 100

        self.vx = 0

    def update(self):

        self.rect.x += self.vx
        self.power -= .12
        if self.power < 0: self.power = 0
        if self.power > 100: self.power = 100

        if self.rect.right > WIDTH - 80:
            self.rect.right = WIDTH - 80
        elif self.rect.left < 75:
            self.rect.left = 75
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.vx = +15
        elif keys[pygame.K_LEFT]:
            self.vx = -15
        else:
            self.vx = 0
        self.mask = pygame.mask.from_surface(self.image)


class Cars(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = CARS_LAYER
        self.groups = game.all_sprites, game.cars
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = POLICE_IM
        self.game = game

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2  # random.randint(90, WIDTH - 180)
        self.rect.y = random.randint(-1000, -500)
        self.vx = 0
        self.vy = random.randrange(8, 17)

    def update(self):
        self.rect.y += self.vy
        if self.rect.top > HEIGHT:
            self.vy = random.randrange(8, 17)
            self.rect.centerx = WIDTH / 2  # random.randint(90, WIDTH - 180)
            self.rect.y = random.randint(-1000, -500)
        self.mask = pygame.mask.from_surface(self.image)


class Cars2(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = CARS_LAYER
        self._layer = CARS_LAYER
        self.groups = game.all_sprites, game.cars
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = random.choice(Cars_im)

        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(90, WIDTH / 2 - 60)
        self.rect.y = random.randint(-500, -200)
        self.vx = 0
        self.vy = random.randrange(8, 17)

    def update(self):
        self.rect.y += self.vy
        if self.rect.top > HEIGHT:
            self.vy = random.randrange(8, 17)
            self.image = random.choice(Cars_im)
            self.rect.x = random.randint(90, WIDTH / 2 - 60)
            self.rect.y = random.randint(-500, -200)
            self.mask = pygame.mask.from_surface(self.image)


class Cars3(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = CARS_LAYER
        self.groups = game.all_sprites, game.cars
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = random.choice(Cars_im)
        self.game = game

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH / 2 + 30, WIDTH - 150)
        self.rect.y = random.randint(-500, -50)
        self.vx = 0
        self.vy = random.randrange(10, 17)

    def update(self):
        self.rect.y += self.vy
        if self.rect.top > HEIGHT:
            self.vy = random.randrange(8, 17)
            self.rect.x = random.randint(WIDTH / 2 + 30, WIDTH - 180)
            self.rect.y = random.randint(-500, -50)
        self.mask = pygame.mask.from_surface(self.image)


class Guide(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = GUIDE_LAYER
        self.groups = game.all_sprites, game.guides
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = CHAR
        self.rect = self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 470  # 439
        self.vx = 0
        self.vy = -8
        self.guide_timer = pygame.time.get_ticks()

    def update(self):
        self.rect.y += self.vy
        now = pygame.time.get_ticks()
        if now - self.guide_timer > 5000:
            self.vy = +8
            self.guide_timer = now
        if self.rect.y <= 428:
            self.rect.y = 428


class Fuel(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.fuels
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = TANK
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(92, 461)
        self.rect.y = random.randrange(-200, -500, -1)
        self.vx = 0
        self.vy = 9

    def update(self):
        self.rect.y += self.vy
        if self.rect.top > HEIGHT:
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(92, 461)
            self.rect.y = random.randint(-1000, -300)
            self.vy = random.randrange(6, 11)
        self.mask = pygame.mask.from_surface(self.image)
