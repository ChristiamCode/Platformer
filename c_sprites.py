# Sprite classes

import pygame as pg
from vars import *

vec = pg.math.Vector2

class plr(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20,20))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.v = vec(0, 0)
        self.a = vec(0, 0)
    def update(self):
        self.a = vec(0, 0.4)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.a.x = -acceleration
        if keys[pg.K_d]:
            self.a.x = acceleration
        # Apply deceleration
        self.a.x += self.v.x * deceleration
        self.v += self.a
        self.pos += self.v + 0.5 * self.a
        self.rect.midbottom = self.pos

class terrain(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(skin)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
