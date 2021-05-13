from sys import exit

import pygame
from pygame.sprite import Sprite

from settings import SHIPSPEED, BULLETCOLOR, BULLETHEIGHT, BULLETSPEED, BULLETWIDTH


class Ship:
    def __init__(self, aiGame):
        self.screen = aiGame.screen
        self.screenRect = aiGame.screen.get_rect()

        self.image = pygame.image.load("img/ship13.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screenRect.midbottom

        self.movingRight = False
        self.movingLeft = False
        self.x = float(self.rect.x)

    def update(self):
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.x += SHIPSPEED
        elif self.movingLeft and self.rect.left > 0:
            self.x -= SHIPSPEED
        self.rect.x = self.x

    def blit_me(self):
        try:
            self.screen.blit(self.image, self.rect)
        except KeyboardInterrupt:
            exit(0)


class Bullet(Sprite):
    def __init__(self, aiGame):
        super().__init__()

        self.screen = aiGame.screen
        self.color = BULLETCOLOR
        self.rect = pygame.Rect(0, 0, BULLETWIDTH, BULLETHEIGHT)
        self.rect.midtop = aiGame.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= BULLETSPEED
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
