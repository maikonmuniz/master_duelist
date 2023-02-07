import pygame

print("Ola mundo")

pygame.init()

largura = 900
altura  = 700

tela =  pygame.display.set_mode((largura, altura))


clock = pygame.time.Clock()

FPS = 40
fundo         = pygame.image.load("imagens/fundo.png")
fundo_desenho = pygame.image.load("imagens/img_inicio.jpg")


rodano = True

while rodano:
    pygame.transform.scale(fundo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodano = False

    # tela.blit(fundo_desenho, (0, 40))
    tela.blit(fundo, (30, 15))

    pygame.display.update()

pygame.quit()