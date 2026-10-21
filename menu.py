import pygame
import sys
import utils as u
import reader as r

pygame.init()

# Ideias:
# Botão para retomar onde parou: manda a informação do último quadrinho lido e página para um arquivo de log/salvamento
# Botão Biblioteca
# Botão Sair

def Menu():
    btns = ["play","quit"]
    selected = 0
    while True:
        u.screen.fill(u.WHITE)

        play_btn = pygame.Rect(250,200,140,50)
        quit_btn = pygame.Rect(250,300,140,50)

        pygame.draw.rect(u.screen, u.LIGHT if selected == 0 else u.DARK, play_btn)
        pygame.draw.rect(u.screen, u.LIGHT if selected == 1 else u.DARK, quit_btn)

        play_text = u.text("Play")
        quit_text = u.text("Quit")

        u.screen.blit(play_text, (275, 200))
        u.screen.blit(quit_text, (275, 300))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    selected = (selected + 1) % len(btns)
                if e.key == pygame.K_DOWN:
                    selected = (selected - 1) % len(btns)
                elif e.key == pygame.K_KP_ENTER or e.key == pygame.KSCAN_KP_ENTER:
                    if selected == 0:
                        r.Reader() 
                    else:
                        pygame.quit()
                        sys.exit()     
                

        pygame.display.update()                       

Menu()

pygame.quit()    