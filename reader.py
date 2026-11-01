import pygame
import utils as u
import sys
import pymupdf

# Interessante:
# Usar yield para ler as páginas do quadrinho

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

            if e.type == pygame.KEYDOWN:
                
                if e.key == pygame.K_RIGHT:
                    nova = min(pagina + 1, len(hq) - 1)
                    print(nova)
                
                elif e.key == pygame.K_LEFT:
                    nova = max(pagina - 1, 0 )
                    print(nova)

                else:
                    nova = pagina 

                if nova != pagina:
                    pagina = nova
                    img = carregar_pagina(hq, pagina)
                    scroll_y = max(0, min(0, max_scroll))
                    print(f"Pag {pagina}")
                        

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_DOWN]:
            scroll_y += 2
            nova = pagina
            
        if teclas[pygame.K_UP]:
            scroll_y -= 2
            nova = pagina   
        
        u.screen.fill((u.DARK))
        u.screen.blit(img, (0, -scroll_y))    

        pygame.display.update()                    


Reader()       