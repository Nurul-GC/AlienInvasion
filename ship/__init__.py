import pygame
from sys import exit


class SHIP:
    def __init__(self, aiGame):
        self.screen = aiGame.screen
        self.screenRect = aiGame.screen.get_rect()

        self.image = pygame.image.load("img/ship13.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screenRect.midbottom

    def blit_me(self):
        try:
            self.screen.blit(self.image, self.rect)
        except KeyboardInterrupt:
            exit(0)
