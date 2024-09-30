class Item:
    def __init__(self, nome, tipo, dano=0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
def itens_disp():

    from random import choice
    itens_possiveis = [
        Item("Galaxy Note 7", "Arma", 25),
        Item("Poção de Vida", "Consumível"),
        Item("Espada Curta", "Arma", 10),
        Item("Espada Longa", "Arma", 15),
        Item("Machado de Batalha", "Arma", 20),
        Item("Elixir de Mana", "Consumível"),
        Item("Arco Curto", "Arma", 12),
        Item("Flechas Infinitas", "Acessório"),
        Item("Poção de Invisibilidade", "Consumível"),
        Item("Escudo de Bronze", "Defesa"),
        Item("Elmo de Aço", "Equipamento"),
        Item("Anel de Regeneração", "Acessório"),
        Item("Poção de Cura Rápida", "Consumível"),
        Item("Bastão de Magia", "Arma", 18),
        Item("Adaga Envenenada", "Arma", 8),
        Item("Cota de Malha", "Defesa"),
        Item("Botas da Velocidade", "Equipamento"),
        Item("Chave do Cofre", "Especial"),
        Item("Espada Flamejante", "Arma", 25),
        Item("Livro de Magias", "Consumível"),
        Item("Poção de Resistência", "Consumível"),
        Item("Lança de Ouro", "Arma", 30),
        Item("Escudo de Cristal", "Defesa"),
        Item("Armadura de Dragão", "Equipamento"),
        Item("Amuleto da Sorte", "Acessório")
    ]

    return choice(itens_possiveis)