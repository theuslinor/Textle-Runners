class ItemConsumivel:
    def __init__(self, nome, tipo, dano=0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
def itens_disp():

    from random import choice
    itens_possiveis = [
        ItemConsumivel("Poção de Vida", "Consumível"),
        ItemConsumivel("Elixir de Mana", "Consumível"),
        ItemConsumivel("Poção de Invisibilidade", "Consumível"),
        ItemConsumivel("Poção de Cura Rápida", "Consumível"),
        ItemConsumivel("Poção de Resistência", "Consumível"),
        ItemConsumivel("Livro de Magias", "Consumível")
    ]

    return choice(itens_possiveis)
