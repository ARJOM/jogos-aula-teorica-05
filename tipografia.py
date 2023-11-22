import pygame

pygame.init()

nome = "Informática Aplicada à Jogos Digitais"

fonte = pygame.font.SysFont("arial", 64)
superficie_do_nome = fonte.render(nome, True, (0,0,0), (255, 255, 255))
pygame.image.save(superficie_do_nome, "assets/name.png")