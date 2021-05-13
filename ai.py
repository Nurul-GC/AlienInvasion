from sys import exit

import pygame

from settings import SCREENWIDTH, SCREENHEIGHT, SCREENCOLOR, BULLETSALLOWED
from ship import Ship, Bullet


class AI:
    def __init__(self):
        pygame.init()

        # propriedades da janela (dimensão-titulo)
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("GC - AlienInvasion")

        # componentes do jogo
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def runGame(self):
        """o nome da função ja diz tudo.. (^_^)"""
        while True:
            self.checkEvent()
            self.ship.update()
            self.updateBullets()
            self.updateScreen()

    def checkEvent(self):
        """verifica e valida as interações do usuario com a aplicação"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.KEYDOWN:
                self.keyDown(event)
            elif event.type == pygame.KEYUP:
                self.keyUP(event)

    def keyUP(self, _event):
        """verifica a interação do usuario pressionando uma tecla

        :param _event: a instancia de eventos da framework
        """
        if _event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
        elif _event.key == pygame.K_LEFT:
            self.ship.movingLeft = False

    def keyDown(self, _event):
        """verifica a interação do usuario largando a tecla pressionada

        :param _event: a instancia de eventos da framework
        """
        if _event.key == pygame.K_RIGHT:
            self.ship.movingRight = True
        elif _event.key == pygame.K_LEFT:
            self.ship.movingLeft = True
        elif _event.key == pygame.K_q:
            exit(0)
        elif _event.key == pygame.K_SPACE or pygame.K_UP:
            self.fireBullet()

    def fireBullet(self):
        """cria e armazena a bala disparada pela nave"""
        if len(self.bullets) < BULLETSALLOWED:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def updateBullets(self):
        """verifica e atualiza o estado das balas disparadas pelo usuario"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def updateScreen(self):
        """verifica e atualiza o estado da janela"""
        self.screen.fill(SCREENCOLOR)
        self.ship.blit_me()
        for bullet in self.bullets.sprites():
            bullet.drawBullet()
        pygame.display.flip()


if __name__ == '__main__':
    aiApp = AI()
    aiApp.runGame()
