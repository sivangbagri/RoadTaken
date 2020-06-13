"""
Author: Shivang
Purpose: RoadTaken pygame
Started on: 7/4/20
Completed on: 18/4/20
"""

import pygame
import time
import random
from road_setting import *

from road_sprites import *


class Game:

    def __init__(self):

        # initialize game window, etc

        pygame.init()

        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.running = True

    def new(self):

        # start a new game

        self.all_sprites = pygame.sprite.Group()
        self.cars = pygame.sprite.Group()
        self.guides = pygame.sprite.Group()
        self.fuels = pygame.sprite.Group()
        self.player = Player()

        self.all_sprites.add(self.player)
        Cars(self)
        Cars2(self)
        Cars3(self)

        Fuel(self)

        self.blow = pygame.mixer.Sound('road_assets/horn.wav')
        self.passby = pygame.mixer.Sound('road_assets/passby.wav')
        self.passby.set_volume(0.1)
        self.hit = pygame.mixer.Sound('road_assets/boo.wav')
        self.ciren = pygame.mixer.Sound("road_assets/hitt.wav")
        self.collect = pygame.mixer.Sound("road_assets/sfx_point.wav")

        self.run()

    def run(self):

        # Game Loop

        self.playing = True

        while self.playing:
            self.clock.tick(FPS)

            self.events()

            self.update()

            self.draw()

    def update(self):

        # Game Loop - Update

        hits = pygame.sprite.spritecollide(self.player, self.cars, True, pygame.sprite.collide_mask)
        if hits:
            self.hit.play()
            self.playing = False
        if random.randrange(10) == 2:
            self.ciren.play()
            self.passby.play()
        else:
            self.ciren.stop()
        hit = pygame.sprite.spritecollide(self.player, self.fuels, True, pygame.sprite.collide_mask)
        if hit:
            Fuel(self)
            self.player.power += 5

            self.collect.play()
        if self.player.power == 0:
            self.playing = False
        self.all_sprites.update()

    def events(self):

        # Game Loop - events

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.blow.play()

            # check for closing window

            if event.type == pygame.QUIT:

                if self.playing:
                    self.playing = False

                self.running = False

    def draw_shield(self, x, y, pct):
        if pct < 0: pct = 0
        bar_length = 100
        bar_height = 30
        fill = pct
        out_rect = pygame.Rect(x, y, bar_length, bar_height)
        fill_rect = pygame.Rect(x, y, fill, bar_height)
        pygame.draw.rect(self.screen, GREEN, fill_rect)
        pygame.draw.rect(self.screen, BLACK, out_rect, 2)
        if pct < 27:
            pygame.draw.rect(self.screen, RED, fill_rect)
            pygame.draw.rect(self.screen, BLACK, out_rect, 2)

    def draw(self):

        # Game Loop - draw

        self.screen.fill(BLACK)

        self.screen.blit(back_im, (0, 0))
        g.draw_shield(35, 14, self.player.power)
        s = pygame.Surface((1000, 750))
        s.set_alpha(25)
        opa_lst = [WHITE, BLACK]
        s.fill(random.choice(opa_lst))
        self.screen.blit(s, (0, 0))

        self.screen.blit(PED, (373, 216))
        self.screen.blit(FUEL, (-10, 0))

        self.all_sprites.draw(self.screen)

        # *after* drawing everything, flip the display

        pygame.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.blit(START_BG, (0, 0))
        # self.screen.fill(Aqua)
        self.screen.blit(INTRO, (135, 130))
        self.start_rect = pygame.draw.rect(self.screen, RED, (205, 430, 150, 40))
        self.quit_rect = pygame.draw.rect(self.screen, RED, (205, 480, 150, 40))
        self.draw_text("START GAME", 26, WHITE, 279, 433)
        self.draw_text("QUIT GAME", 26, WHITE, 279, 483)
        pygame.display.flip()
        self.wait_for_key()

    def show_middle_screen(self):
        # game splash/start screen

        self.screen.blit(MIDDLE_BG, (0, 0))
        self.draw_text("A Driver is on his way, but it does't seems easy!.You have to ", 21, BLACK, 290,
                       HEIGHT / 2 - 50)
        self.draw_text("reach home with limited fuel ASAP!", 21, BLACK, 290, HEIGHT / 2 - 30)
        self.draw_text("Remember don't be a BADASS and drive carefully!", 21, BLACK, 290, HEIGHT / 2 - 10)
        self.draw_text("---Press any key to proceed!---", 21, BLACK, 290, HEIGHT - 25)
        pygame.display.flip()
        self.wait_for_middle()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.blit(END, (0, 0))
        pygame.draw.rect(self.screen, WHITE, (0, HEIGHT / 2 - 10, WIDTH, 53))
        self.draw_text("GAME OVER", 50, BLACK, WIDTH / 2, HEIGHT / 2 - 10)
        pygame.draw.rect(self.screen, BLACK, (0, HEIGHT - 30, WIDTH, 53))
        self.draw_text("-By Shivang", 25, WHITE, WIDTH / 2, HEIGHT - 30)
        pygame.display.flip()
        self.wait_for_go()

    def wait_for_middle(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def wait_for_go(self):

        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False

    def wait_for_key(self):

        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if self.start_rect.collidepoint(pos):
                        waiting = False

                    if self.quit_rect.collidepoint(pos):
                        waiting = False
                        self.running = False
                        pygame.quit()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font('road_assets/BRLNSR.TTF', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()

g.show_start_screen()
try:
    g.show_middle_screen()
except pygame.error as e:
    pass

while g.running:
    g.new()

    g.show_go_screen()

pygame.quit()
