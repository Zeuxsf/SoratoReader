import pygame
import sys
import utils as u
import reader as r

pygame.init()

def Menu():
    pos = "up"
    while True:
        u.screen.fill(u.WHITE)

        play_btn = pygame.Rect(250,200,140,50)
        quit_btn = pygame.Rect(250,300,140,50)

        pygame.draw.rect(u.screen, u.LIGHT if pos == "up" else u.DARK, play_btn)
        pygame.draw.rect(u.screen, u.LIGHT if pos == "down" else u.DARK, quit_btn)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    pos = "up"
                if e.key == pygame.K_DOWN:
                    pos = "down" 
                elif e.key == pygame.K_KP_ENTER or e.key == pygame.KSCAN_KP_ENTER:
                    if pos == "up":
                        r.Reader() 
                    else:
                        pygame.quit()
                        sys.exit()       

        pygame.display.update()                       

Menu()

pygame.quit()    