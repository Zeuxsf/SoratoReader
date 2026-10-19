import pygame
import utils as u
import sys

def Reader():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        u.screen.fill((u.YELLOW))

        font = pygame.font.SysFont("Arial", 40)
        text = font.render("Lendo Quadrinhos...", True, u.DARK)
        u.screen.blit(text, (120,240))
        pygame.display.update()
