import sys

import pygame
from pygame.locals import *

pygame.init()


class Jogador:

    def __init__(self, image_path, x, y):
        self.image = pygame.transform.scale( pygame.image.load(image_path).convert(), (50, 80))
        self.x = x
        self.y = y
        # self.hitbox = (x+20, y)

    def direita(self):
        self.x += 0.5

    def esquerda(self):
        self.x -= 0.5

    def collide(self, obj: Rect):
        a = Rect((self.x, self.y), (50, 80))
        return a.colliderect(obj)

nome_background = 'fundo.jpg'
tamanho=(800,600)
mensagem = "Encostou"
font = pygame.font.SysFont("arial", 99)
superficie_de_texto = font.render(mensagem, True, (0,0,255))


tela = pygame.display.set_mode(tamanho)
background = pygame.image.load(nome_background).convert()

jogador = Jogador('assets/token.jpg', 0, 250)


if __name__.endswith('__main__'):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            jogador.esquerda()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            jogador.direita()

        tela.blit(background, (0, 0))
        tela.blit(jogador.image, (jogador.x, jogador.y))
        a = pygame.draw.rect(tela, (94, 33, 41), Rect((295, 200), (50, 80)))

        if jogador.collide(a):
            tela.blit(superficie_de_texto, (0, 0))

        pygame.display.update()