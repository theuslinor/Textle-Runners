class ItemConsumivel:
    def __init__(self, nome, tipo, dano=0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
def itens_disp_consumiveis():

    from random import choice
    itens_possiveis = [
        ItemConsumivel("Poção de Vida", "Consumível"),
    ]

    return choice(itens_possiveis)
