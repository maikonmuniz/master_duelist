
import pygame
from pygame.locals import *
from card import Card

pygame.init()

largura = 900
altura  = 700

tela =  pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

fundo         = pygame.image.load("imagens/tela_game_2.jpg")
fundo_desenho = pygame.image.load("imagens/img_inicio.jpg")

rodano = True

exodia = Card("Dark Magician", 123123, 123123, "imagens/cards/dark_magician.jpg")

posicao_dict = {"posicao_5": (630, 430),
                "posicao_4": (527, 430),
                "posicao_3": (425, 430),
                "posicao_2": (324, 430),
                "posicao_1": (222, 430)}

direct_img = pygame.image.load("imagens/card.jpg")
position_deck = 400

cont = 0

cartas_campo_lado2 = ["imagens/cards/aladora.jpg", "imagens/cards/dark_magician.jpg", "imagens/cards/dragon_of_azuis.png", "imagens/cards/obelisk.png", "imagens/cards/slifertheSkyDragon.png"]


list_cards_campo_lado2 = []
for cards_indice in cartas_campo_lado2:
    list_cards_campo_lado2.append(pygame.image.load(cards_indice))

def card_campo_lado_2(x, posicao_card):
    return tela.blit(pygame.transform.scale(list_cards_campo_lado2[x], (60, 90)), posicao_card)

while rodano:

    clock.tick(4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodano = False

    pygame.transform.scale(fundo, (0, 0))

    tela.blit(fundo, (0, 0))

    x = 0

    # card campo lada 1
    for posicao_card in posicao_dict.values():

        card_campo_lado_2(x, posicao_card)


        x += 1
    
    tela.blit(direct_img, (738, 550))

    pygame.display.update()

pygame.quit()
