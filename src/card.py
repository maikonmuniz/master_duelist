

class Card:

    def __init__(self, nome, ataque, defesa):
        self.__nome      = nome
        self.__ataque    = ataque
        self.__defesa    = defesa
        self.modo_ataque = modo_ataque
        self.modo_defesa = modo_defesa
    
    def modo_ataque(self):
        
        if self.modo_defesa:
            self.modo_ataque = True
            self.modo_defesa = False

    def modo_defesa(self):

        if self.mode_ataque:
            self.modo_defesa = True
            self.modo_ataque = False