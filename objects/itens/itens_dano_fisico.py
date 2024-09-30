class ItemDanoPhys:
    def __init__(self, nome, tipo, dano=0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
def itens_disp():

    from random import choice
    itens_possiveis = [
        ItemDanoPhys("Galaxy Note 7", "Arma", 25),
        ItemDanoPhys("Espada Curta", "Arma", 10),
        ItemDanoPhys("Espada Longa", "Arma", 15),
        ItemDanoPhys("Machado de Batalha", "Arma", 20),
        ItemDanoPhys("Arco Curto", "Arma", 12),
        ItemDanoPhys("Bastão de Magia", "Arma", 18),
        ItemDanoPhys("Adaga Envenenada", "Arma", 8),
        ItemDanoPhys("Cota de Malha", "Defesa"),
        ItemDanoPhys("Espada Flamejante", "Arma", 25),
        ItemDanoPhys("Lança de Ouro", "Arma", 30),
    ]

    return choice(itens_possiveis)



