
class Card:

    def __init__(self, nome, ataque, defesa, imagem_card):
        self.nome        = nome
        self.ataque      = ataque
        self.defesa      = defesa
        self.modo_ataque = False
        self.modo_defesa = False
        self.imagem_card = imagem_card

    def modo_ataque(self):

        if self.modo_defesa:
            self.modo_ataque = True
            self.modo_defesa = False

    def modo_defesa(self):

        if self.mode_ataque:
            self.modo_defesa = True
            self.modo_ataque = False
