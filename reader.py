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
    scroll_y = 0
    pagina = 0
    img = carregar_pagina(hq,pagina)
    while True:

        u.screen.fill((u.DARK))
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                
                if e.key == pygame.K_RIGHT:
                    nova = min(pagina + 1, len(hq) - 1)
                    print(nova)
                
                if e.key == pygame.K_LEFT:
                    nova = max(pagina - 1, 0 )
                    print(nova)

                if nova != pagina:
                    pagina = nova
                    img = carregar_pagina(hq, pagina)
                    scroll_y = 0
                    print(f"Pag {pagina}")
        u.screen.blit(img, (0, -scroll_y))    

        pygame.display.update()                    