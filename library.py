import os 
import pygame
import utils as u
from reader import Reader

lib_hud = pygame.image.load("images/LIB.bmp")
colecao_img = pygame.image.load("images/colecao.bmp")
livro_img = pygame.image.load("images/livro.bmp")
favorito_img = pygame.image.load("images/favorito.bmp")


largura, altura = 640, 480
altura_linha = 32
topo = 70
linhas_visiveis = (altura - topo) // altura_linha

base = os.path.dirname(os.path.abspath(__file__))
raiz = os.path.join(base, "Library")
os.makedirs(raiz, exist_ok=True)

def listar(pasta):
    colecoes = []
    pdfs = []
    for entrada in os.scandir(pasta):
        if entrada.is_dir():
            colecoes.append((entrada.name, entrada.path, True))
        elif entrada.name.lower().endswith(".pdf"):
            pdfs.append((entrada.name, entrada.path, False))

    colecoes.sort(key=lambda i: i[0].lower())
    pdfs.sort(key=lambda i: i[0].lower())
    itens = colecoes + pdfs
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
                        caminho = os.path.relpath(caminho, os.path.dirname(raiz))
                        Reader(caminho)
                        pygame.event.clear()
                elif e.key == pygame.K_BACKSPACE:
                    if pasta == raiz:
                        return
                    pasta = os.path.dirname(pasta)
                    itens = listar(pasta)
                    selecionado = 0
                    inicio = 0
               
                elif e.key == pygame.K_f and itens:
                    nome, caminho, is_pasta = itens[selecionado]
                    caminho = os.path.relpath(caminho, os.path.dirname(raiz))

                    try:
                        dados = u.load_json()

                        if caminho not in dados:
                            if not is_pasta:
                                dados[caminho] = [True, 0, False]
                                u.save_json(dados)
                        elif dados[caminho][0] == True:
                            dados[caminho][0] = False
                            u.save_json(dados)
                        else:
                            dados[caminho][0] = True
                            u.save_json(dados)    
                    except:
                        dados = {}
                        dados[caminho] = [True, 0, False]
                        u.save_json(dados)

   
                    

            if selecionado < inicio:
                inicio = selecionado
            elif selecionado >= inicio + linhas_visiveis:
                inicio = selecionado - linhas_visiveis + 1            

        u.screen.fill(u.DARK)
        u.screen.blit(lib_hud, (0,0))

        if not itens:
            u.screen.blit(fonte.render(" :( ", True, u.WHITE), (20, topo))

        for i, (nome, caminho, is_pasta) in enumerate(itens[inicio:inicio + linhas_visiveis]):
            caminho = os.path.relpath(caminho, os.path.dirname(raiz))
            real = inicio + i
            if real == selecionado:
                cor = u.WHITE
                if is_pasta:
                    cor = u.INDIGO
            elif is_pasta:
                cor = u.MARINE
            else:
                cor = u.LIGHT

            lateral = topo + i * altura_linha
            if is_pasta:
                u.screen.blit(u.resize_icon(colecao_img,24,24), (30, lateral))
            else:
                try:
                    dados = u.load_json()
                except:
                    dados = {}

                if caminho in dados:
                    if dados[caminho][0] == True:
                        u.screen.blit(u.resize_icon(favorito_img,20,20), (30, lateral))
                    else:
                        u.screen.blit(u.resize_icon(livro_img,20,20), (30, lateral))
                else:
                    u.screen.blit(u.resize_icon(livro_img,20,20), (30, lateral))        

            titulo = os.path.splitext(nome)[0]
            u.screen.blit(fonte.render(titulo, True, cor), (30 + 24 + 8, lateral))

        pygame.display.flip()
        fps.tick(30)


def main():
    pygame.init()    
    navegador()
    pygame.quit()

if __name__ == "__main__":
    main()
        