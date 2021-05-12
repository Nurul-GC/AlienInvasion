from sys import exit
import pygame


class AI:
    def __init__(self):
        pygame.init()

        # propriedades da janela (dimensaoX)
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("GC - AlienInvasion")

    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

            pygame.display.flip()


if __name__ == '__main__':
    aiApp = AI()
    aiApp.runGame()
