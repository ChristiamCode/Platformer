# Basic structure for pygame
import pygame as pg
import random

from c_sprites import *
from vars import *

# Game loop variables
running = True
playing = True

# Game class
class platForm:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    def new(self):
        # Sprite groups
        self.a_sprites = pg.sprite.Group()
        self.landscape = pg.sprite.Group()

        # Objects in groups
        p1 = terrain(WIDTH / 2.25, HEIGHT / 1.2, 100, 40)

        # Adding sprites
        self.a_sprites.add(plr())
        self.a_sprites.add(p1)
        self.landscape.add(p1)
        self.g_loop()

    def g_loop(self):
        global playing
        global running
        while playing:
            self.clock.tick(FRAMES)
            self.events()
            self.update()
            self.make()

    def hit(self):
        plr().pos.y = collide[0].rect.top
        plr().vel.y = 0
    def update(self):
        # Update display
        self.a_sprites.update()
        # Fixed error. Removed collision.py 
        if pg.sprite.spritecollide(plr(),terrain(),False):
            self.hit()
            print("hit")

    def events(self):
        global playing
        global running
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if playing:
                    playing = False
                running = False
    def make(self):
        # Make sprites
        self.screen.fill(bg)
        # Draw sprites
        self.a_sprites.draw(self.screen)
        # Flip the screen(640x480 window)
        pg.display.flip()
    def start_screen(self):
        pass
    def show_start_screen(self):
        pass
    def end_screen(self):
        pass
platForm().start_screen()

# Running loop
while running:
    platForm().new()
    platForm().start_screen()
pg.quit()
