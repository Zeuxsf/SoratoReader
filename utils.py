import pygame

# Configurações
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

# Cores
WHITE = (255,255,255)
LIGHT = (170,170,170)
DARK = (100,100,100)
YELLOW = (255,255,0)

# Texto
def text(msg: str):
    font = pygame.font.SysFont("Arial", 40)
    text = font.render(msg, True, DARK)
    return text