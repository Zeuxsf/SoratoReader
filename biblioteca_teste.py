import os 
import pygame
import utils as u
from reader import Reader

lib = pygame.image.load("images/LIB.bmp")

largura, altura = 640, 480
altura_linha = 32
topo = 70
linhas_visiveis = (altura - topo) // altura_linha

base = os.path.dirname(os.path.abspath(__file__))
raiz = os.path.join(base, "HQs")
os.makedirs(raiz, exist_ok=True)

def listar(pasta):
    pastas = []
    pdfs = []
    for entrada in os.scandir(pasta):
        if entrada.is_dir():
            pastas.append((entrada.name, entrada.path, True))
        elif entrada.name.lower().endswith(".pdf"):
            pdfs.append((entrada.name, entrada.path, False))

    pastas.sort(key=lambda i: i[0].lower())
    pdfs.sort(key=lambda i: i[0].lower())
    itens = pastas + pdfs
    if pasta != raiz:
        itens.insert(0, ("..", os.path.dirname(pasta), True))
    return itens


def navegador():
    fps = pygame.time.Clock()
    pasta = raiz
    itens = listar(pasta)
    selecionado = 0
    inicio = 0
    fonte = pygame.font.SysFont(None, 28)


    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN and itens:
                    selecionado = (selecionado + 1) % len(itens)
                elif e.key == pygame.K_UP and itens:
                    selecionado = (selecionado - 1) % len(itens)
                elif e.key == pygame.K_RETURN and itens:
                    nome, caminho, is_pasta = itens[selecionado]
                    if is_pasta:
                        pasta = caminho
                        itens = listar(pasta)
                        selecionado = 0
                        inicio = 0
                    else:
                        Reader(caminho)
                        pygame.event.clear()
                elif e.key == pygame.K_ESCAPE:
                    if pasta == raiz:
                        return
                    pasta = os.path.dirname(pasta)
                    itens = listar(pasta)
                    selecionado = 0
                    inicio = 0

            if selecionado < inicio:
                inicio = selecionado
            elif selecionado >= inicio + linhas_visiveis:
                inicio = selecionado - linhas_visiveis + 1            

        u.screen.fill(u.DARK)
        u.screen.blit(lib, (0,0))

        if not itens:
            u.screen.blit(fonte.render("Nenhum PDF aqui", True, u.WHITE), (20, topo))

        for i, (nome, caminho, is_pasta) in enumerate(itens[inicio:inicio + linhas_visiveis]):
            real = inicio + i
            if real == selecionado:
                cor = u.WHITE
                if is_pasta:
                    cor = (66, 108, 245)
            elif is_pasta:
                cor = u.LIGHT
            else:
                cor = u.LIGHT
            texto = nome + "/" if is_pasta else nome
            u.screen.blit(fonte.render(texto, True, cor), (30, topo + i * altura_linha))

        pygame.display.flip()
        fps.tick(30)


def main():
    pygame.init()    
    navegador()
    pygame.quit()

main()

        