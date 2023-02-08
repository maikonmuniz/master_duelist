import pygame
from card import Card


pygame.init()

largura = 900
altura  = 700

tela =  pygame.display.set_mode((largura, altura))


clock = pygame.time.Clock()

FPS = 40
fundo         = pygame.image.load("imagens/fundo.png")
fundo_desenho = pygame.image.load("imagens/img_inicio.jpg")

rodano = True

exodia = Card("Teste monstro de duelos", 123123, 123123, "imagens/cards/cabeca_exodia.png")
exodia_img = exodia.imagem_card

exodia_img = pygame.image.load(exodia_img)

while rodano:
    pygame.transform.scale(fundo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodano = False

    # tela.blit(fundo_desenho, (0, 40))
    tela.blit(fundo, (30, 15))
    tela.blit(exodia_img, (45, 50))
    pygame.display.update()

pygame.quit()