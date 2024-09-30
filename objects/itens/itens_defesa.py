class ItemDefesa:
    def __init__(self, nome, tipo, dano=0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
def itens_disp():

    from random import choice
    itens_possiveis = [
        ItemDefesa("Armadura de Dragão", "Equipamento"),
        ItemDefesa("Botas da Velocidade", "Equipamento"),
        ItemDefesa("Escudo de Bronze", "Defesa"),
        ItemDefesa("Elmo de Aço", "Equipamento"),
        ItemDefesa("Escudo de Cristal", "Defesa")
    ]

    return choice(itens_possiveis)



