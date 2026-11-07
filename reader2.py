import pygame
import utils as u
import sys
import pymupdf

hud = pygame.image.load("images/HUD.bmp")

modo_dev = True

if modo_dev == False:
    pygame.joystick.init()
    joy = pygame.joystick.Joystick(0)

def carregar_pagina(hq, n):
    page = hq[n]
    zoom = 640 / page.rect.width
    pixel = page.get_pixmap(matrix=pymupdf.Matrix(zoom,zoom), alpha = False)
    return pygame.image.frombuffer(pixel.samples, (pixel.width, pixel.height), "RGB")


def Reader():
    hq = pymupdf.open("HQs/Blue_Book.pdf")
    pagina = 0
    img = carregar_pagina(hq,pagina)
    scroll_y = 0
    exibir_hud = True
    c = 0

    while True:  

        max_scroll = max(0,img.get_height() - u.screen.get_height())
        scroll_y = max(0, min(scroll_y, max_scroll))  

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.JOYBUTTONDOWN:
                
                if e.button == 5:
                    nova = min(pagina + 1, len(hq) - 1)
                
                elif e.button == 4:
                    nova = max(pagina - 1, 0 )

                else:
                    nova = pagina 

                if nova != pagina:
                    pagina = nova
                    img = carregar_pagina(hq, pagina)
                    scroll_y = max(0, min(0, max_scroll))

                if e.button == 12:
                    exibir_hud = False
                    c += 1
                    if c >= 2:
                        exibir_hud = True
                        c = 0

                if e.button == 2:
                    return

                if e.button == 13:
                    pygame.quit()
                    sys.exit()       

            if e.type == pygame.KEYDOWN:
                
                if e.key == pygame.K_RIGHT:
                    nova = min(pagina + 1, len(hq) - 1)
                
                elif e.key == pygame.K_LEFT:
                    nova = max(pagina - 1, 0 )

                else:
                    nova = pagina 

                if nova != pagina:
                    pagina = nova
                    img = carregar_pagina(hq, pagina)
                    scroll_y = max(0, min(0, max_scroll)) 

                if e.key == pygame.K_TAB:
                    exibir_hud = False
                    c += 1
                    if c >= 2:
                        exibir_hud = True
                        c = 0

                if e.key == pygame.K_BACKSPACE:
                    return

                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()              
                    
                        
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_DOWN]:
            scroll_y += 2
            nova = pagina
            
        if teclas[pygame.K_UP]:
            scroll_y -= 2
            nova = pagina 

        if modo_dev == False:
            if joy.get_button(9):
                scroll_y += 8
                nova = pagina
                
            if joy.get_button(8):
                scroll_y -= 8
                nova = pagina   
        
        u.screen.fill((u.DARK))
        u.screen.blit(img, (0, -scroll_y))

        if exibir_hud:
            u.screen.blit(hud, (0,0))    

        pygame.display.update()                    
