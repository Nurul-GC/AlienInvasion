from sys import exit

import pygame

from settings import SCREENWIDTH, SCREENHEIGHT, SCREENCOLOR
from ship import SHIP


class AI:
    def __init__(self):
        pygame.init()

        # propriedades da janela (dimensão-titulo)
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("GC - AlienInvasion")

        # componentes do jogo
        self.ship = SHIP(self)

    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

            self.screen.fill(SCREENCOLOR)
            self.ship.blit_me()
            pygame.display.flip()


if __name__ == '__main__':
    aiApp = AI()
    aiApp.runGame()
