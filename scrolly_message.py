import sys

import pygame
from pygame.locals import *

pygame.init()

nome_background = 'assets/fundo.jpg'
tamanho=(800,600)
mensagem = "Então é Natal. O que você fez?"

tela = pygame.display.set_mode(tamanho)

font = pygame.font.SysFont("arial", 99)
superficie_de_texto = font.render(mensagem, True, (0,0,255))

x = 0
y = ((tamanho[1] - superficie_de_texto.get_height()) / 2)

background = pygame.image.load(nome_background).convert()

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        tela.blit(background, (0, 0))

        x -= 0.5
        if x < -superficie_de_texto.get_width():
            x = 0

        tela.blit(superficie_de_texto, (x, y))
        tela.blit(superficie_de_texto, (x+superficie_de_texto.get_width(), y))
        pygame.display.update()