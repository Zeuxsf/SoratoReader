import pygame

pygame.init()

tela = pygame.display.set_mode((640,480))
fonte = pygame.font.Font(None,28)
fps = pygame.time.Clock()

pygame.joystick.init()
joy = pygame.joystick.Joystick(0)

linhas = []
rodando = True

while rodando:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            rodando = False
        elif e.type ==  pygame.JOYBUTTONDOWN:
            linhas.append(f"btn {e.button}")
        elif e.type ==  pygame.JOYHATMOTION:
            linhas.append(f"hat {e.value}")            
        elif e.type ==  pygame.JOYAXISMOTION and abs(e.value) > 0.5:
            linhas.append(f"eixo {e.axis} = {e.value:.1f}")

    linhas = linhas[-12:]

    tela.fill((0,0,0))
    for i, texto in enumerate(linhas):
        tela.blit(fonte.render(texto, True, (255,255,255)), (20,20 + i * 32))
    pygame.display.flip()
    fps.tick(30)                    