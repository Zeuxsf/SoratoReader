import pygame
import sys
import utils as u
import reader2 as r

pygame.init()

# Ideias:
# Botão para retomar onde parou: manda a informação do último quadrinho lido e página para um arquivo de log/salvamento
# Botão Biblioteca
# Botão Sair

menu = pygame.image.load("images/MENU.bmp")
info = pygame.image.load("images/INFO.bmp")


modo_dev = True

if modo_dev == False:
    pygame.joystick.init()
    joy = pygame.joystick.Joystick(0)

def Menu():
    exibir_info = False
    c = 0
    while True:
        u.screen.fill(u.WHITE)


        u.screen.blit(menu, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_KP_ENTER:
                    r.Reader() 
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if e.key == pygame.K_TAB:
                    c += 1
                    exibir_info = True
                    if c >= 2:
                        exibir_info = False
                        c = 0

        if exibir_info:
            u.screen.blit(info, (0,0))
                

        pygame.display.update()                       

Menu()
