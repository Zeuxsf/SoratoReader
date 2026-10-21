import pygame
import utils as u
import sys

# Interessante:
# Usar yield para ler as páginas do quadrinho


def Reader():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        u.screen.fill((u.YELLOW))

        u.screen.blit(u.text("Lendo Quadrinhos..."), (120,240))
        pygame.display.update()
