import pygame
import json

# Configurações
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
modo_dev = True

# Cores
WHITE = (255,255,255)
LIGHT = (170,170,170)
DARK = (100,100,100)
YELLOW = (255,255,0)
INDIGO = (43, 0, 255)
MARINE = (19, 0, 112)
FAVORITE = (255, 209, 0)

# Texto
def text(msg: str):
    font = pygame.font.SysFont("Arial", 40)
    text = font.render(msg, True, DARK)
    return text

# Imagem
def resize_icon(icon, h, w):
    resized_icon = pygame.transform.smoothscale(icon, (h,w))
    return resized_icon

# Salvamento em JSON
def load_json():
    with open("history.json", "r") as f:
        data = json.load(f)
    return data

def save_json(data):
    with open("history.json", "w") as f:
        json.dump(data, f, indent=4)

def add_json(data):
    with open("history.json", "a") as f:
        json.dump(data, f, indent=4)