import pymupdf
import pygame
import utils as u


doc = pymupdf.open("HQs/Batman_Spiderman.pdf")
print(len(doc))
page = doc[0]
print(page.rect.width, page.rect.height)

zoom = 640 / page.rect.width
pixel = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha= False)

img = pygame.image.frombuffer(pixel.samples, (pixel.width, pixel.height), "RGB")


while True:
    u.screen.fill(u.WHITE)

    u.screen.blit(img, (0, 0))

    pygame.display.update()