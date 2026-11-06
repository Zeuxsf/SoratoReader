import pygame
import utils as u
import sys
import pymupdf

imagem = pygame.image.load("HUD.bmp")

#pygame.joystick.init()
#joy = pygame.joystick.Joystick(0)

def carregar_pagina(hq, n):
    page = hq[n]
    zoom = 640 / page.rect.width
    pixel = page.get_pixmap(matrix=pymupdf.Matrix(zoom,zoom), alpha = False)
    return pygame.image.frombuffer(pixel.samples, (pixel.width, pixel.height), "RGB")


def Reader():
    hq = pymupdf.open("HQs/Batman_Spiderman.pdf")
    pagina = 0
    img = carregar_pagina(hq,pagina)
    scroll_y = 0

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
                    print(nova)
                
                elif e.button == 4:
                    nova = max(pagina - 1, 0 )
                    print(nova)

                else:
                    nova = pagina 

                if nova != pagina:
                    pagina = nova
                    img = carregar_pagina(hq, pagina)
                    scroll_y = max(0, min(0, max_scroll))
                    print(f"Pag {pagina}")
                    
                        

        if joy.get_button(9):
            scroll_y += 2
            nova = pagina
            
        if joy.get_button(8):
            scroll_y -= 2
            nova = pagina   
        
        u.screen.fill((u.DARK))
        u.screen.blit(img, (0, -scroll_y))
        u.screen.blit(imagem, (0,0))    

        pygame.display.update()                    


