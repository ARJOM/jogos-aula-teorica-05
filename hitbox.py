import sys

import pygame
from pygame.locals import *

pygame.init()

nome_background = 'fundo.jpg'
tamanho=(800,600)
mensagem = "Encostou"

tela = pygame.display.set_mode(tamanho)

font = pygame.font.SysFont("arial", 99)
superficie_de_texto = font.render(mensagem, True, (0,0,255))

background = pygame.image.load(nome_background).convert()

tela.blit(background, (0, 0))

a_x = 295
b_x = 700

if __name__.endswith('__main__'):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        tela.blit(background, (0, 0))

        a = pygame.draw.rect(tela, (94, 33, 41), Rect((a_x, 200), (50, 80)))
        b = pygame.draw.rect(tela, (94, 33, 41), Rect((b_x, 280), (50, 80)))

        if a.colliderect(b):
            tela.blit(superficie_de_texto, (0, 0))
        else:
            b_x -= 0.2






        # b.x -= 1

        # tela.blit(superficie_de_texto, (x, y))
        # tela.blit(superficie_de_texto, (x+superficie_de_texto.get_width(), y))
        pygame.display.update()