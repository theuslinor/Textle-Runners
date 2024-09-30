class ItemDanoPhys:
    def __init__(self, nome, tipo, dano=0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
def itens_disp():

    from random import choice
    itens_possiveis = [
        ItemDanoPhys("Espada Curta", "Arma", 10),
        ItemDanoPhys("Machado de Guerra", "Arma", 15),
        ItemDanoPhys("Lança Longa", "Arma", 12),
        ItemDanoPhys("Martelo de Batalha", "Arma", 20),
        ItemDanoPhys("Adaga Afiada", "Arma", 8),
        ItemDanoPhys("Espada Longa", "Arma", 18),
        ItemDanoPhys("Clava Pesada", "Arma", 14),
        ItemDanoPhys("Foice Sombria", "Arma", 22),
        ItemDanoPhys("Tridente de Ferro", "Arma", 13),
        ItemDanoPhys("Katana", "Arma", 17),
        ItemDanoPhys("Machadinha", "Arma", 11),
        ItemDanoPhys("Maça de Ferro", "Arma", 16),
        ItemDanoPhys("Espada Flamejante", "Arma", 25),
        ItemDanoPhys("Bastão Arcano", "Arma", 9),
        ItemDanoPhys("Cajado da Tempestade", "Arma", 21),
        ItemDanoPhys("Sabre de Luz", "Arma", 23),
        ItemDanoPhys("Espada de Cristal", "Arma", 19),
        ItemDanoPhys("Martelo do Trovão", "Arma", 24),
        ItemDanoPhys("Foice de Ossos", "Arma", 18),
        ItemDanoPhys("Gládio Rúnico", "Arma", 20),

    ]

    return choice(itens_possiveis)



