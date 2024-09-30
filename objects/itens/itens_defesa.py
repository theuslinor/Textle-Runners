class ItemDefesa:
    def __init__(self, nome, tipo, dano, defesa, parte):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.defesa = defesa
        self.parte = parte
def itens_disp():

    from random import choice

    itens_possiveis = [
        ItemDefesa("Capacete de Couro", "Equipamento", 0, 2, "Cabeça"),
        ItemDefesa("Elmo de Ferro", "Equipamento", 0, 5, "Cabeça"),
        ItemDefesa("Capacete de Aço", "Equipamento", 0, 8, "Cabeça"),
        ItemDefesa("Elmo de Dragão", "Equipamento", 2, 12, "Cabeça"),
        ItemDefesa("Capacete de Cristal", "Equipamento", 3, 15, "Cabeça"),
        ItemDefesa("Elmo Sombrio", "Equipamento", 1, 10, "Cabeça"),
        ItemDefesa("Capacete de Prata", "Equipamento", 0, 6, "Cabeça"),
        ItemDefesa("Elmo de Cavaleiro", "Equipamento", 0, 9, "Cabeça"),
        ItemDefesa("Capacete Místico", "Equipamento", 2, 7, "Cabeça"),
        ItemDefesa("Elmo de Titânio", "Equipamento", 4, 14, "Cabeça"),
        ItemDefesa("Capacete Runico", "Equipamento", 2, 13, "Cabeça"),
        ItemDefesa("Elmo de Madeira", "Equipamento", 0, 3, "Cabeça"),
        ItemDefesa("Capacete de Bronze", "Equipamento", 0, 4, "Cabeça"),
        ItemDefesa("Elmo do Berserker", "Equipamento", 3, 11, "Cabeça"),
        ItemDefesa("Capacete Flamejante", "Equipamento", 5, 10, "Cabeça"),


        ItemDefesa("Peitoral de Couro", "Equipamento", 0, 4, "Peito"),
        ItemDefesa("Armadura de Ferro", "Equipamento", 0, 8, "Peito"),
        ItemDefesa("Peitoral de Aço", "Equipamento", 0, 12, "Peito"),
        ItemDefesa("Armadura de Dragão", "Equipamento", 3, 16, "Peito"),
        ItemDefesa("Peitoral de Cristal", "Equipamento", 2, 20, "Peito"),
        ItemDefesa("Armadura Sombria", "Equipamento", 1, 14, "Peito"),
        ItemDefesa("Peitoral de Prata", "Equipamento", 0, 10, "Peito"),
        ItemDefesa("Armadura de Cavaleiro", "Equipamento", 0, 13, "Peito"),
        ItemDefesa("Peitoral Místico", "Equipamento", 2, 12, "Peito"),
        ItemDefesa("Armadura de Titânio", "Equipamento", 4, 18, "Peito"),
        ItemDefesa("Peitoral Runico", "Equipamento", 3, 15, "Peito"),
        ItemDefesa("Armadura de Madeira", "Equipamento", 0, 5, "Peito"),
        ItemDefesa("Peitoral de Bronze", "Equipamento", 0, 7, "Peito"),
        ItemDefesa("Armadura do Berserker", "Equipamento", 3, 14, "Peito"),
        ItemDefesa("Peitoral Flamejante", "Equipamento", 5, 12, "Peito"),


        ItemDefesa("Calças de Couro", "Equipamento", 0, 3, "Pernas"),
        ItemDefesa("Calças de Ferro", "Equipamento", 0, 6, "Pernas"),
        ItemDefesa("Calças de Aço", "Equipamento", 0, 10, "Pernas"),
        ItemDefesa("Calças de Dragão", "Equipamento", 2, 14, "Pernas"),
        ItemDefesa("Calças de Cristal", "Equipamento", 3, 18, "Pernas"),
        ItemDefesa("Calças Sombrias", "Equipamento", 1, 11, "Pernas"),
        ItemDefesa("Calças de Prata", "Equipamento", 0, 8, "Pernas"),
        ItemDefesa("Calças de Cavaleiro", "Equipamento", 0, 9, "Pernas"),
        ItemDefesa("Calças Místicas", "Equipamento", 2, 12, "Pernas"),
        ItemDefesa("Calças de Titânio", "Equipamento", 4, 16, "Pernas"),
        ItemDefesa("Calças Rúnicas", "Equipamento", 3, 13, "Pernas"),
        ItemDefesa("Calças de Madeira", "Equipamento", 0, 4, "Pernas"),
        ItemDefesa("Calças de Bronze", "Equipamento", 0, 6, "Pernas"),
        ItemDefesa("Calças do Berserker", "Equipamento", 3, 10, "Pernas"),
        ItemDefesa("Calças Flamejantes", "Equipamento", 5, 11, "Pernas"),


        ItemDefesa("Botas de Couro", "Equipamento", 0, 2, "Pés"),
        ItemDefesa("Botas de Ferro", "Equipamento", 0, 4, "Pés"),
        ItemDefesa("Botas de Aço", "Equipamento", 0, 7, "Pés"),
        ItemDefesa("Botas de Dragão", "Equipamento", 2, 10, "Pés"),
        ItemDefesa("Botas de Cristal", "Equipamento", 3, 13, "Pés"),
        ItemDefesa("Botas Sombrias", "Equipamento", 1, 9, "Pés"),
        ItemDefesa("Botas de Prata", "Equipamento", 0, 5, "Pés"),
        ItemDefesa("Botas de Cavaleiro", "Equipamento", 0, 6, "Pés"),
        ItemDefesa("Botas Místicas", "Equipamento", 2, 8, "Pés"),
        ItemDefesa("Botas de Titânio", "Equipamento", 4, 12, "Pés"),
        ItemDefesa("Botas Rúnicas", "Equipamento", 3, 11, "Pés"),
        ItemDefesa("Botas de Madeira", "Equipamento", 0, 3, "Pés"),
        ItemDefesa("Botas de Bronze", "Equipamento", 0, 4, "Pés"),
        ItemDefesa("Botas do Berserker", "Equipamento", 3, 9, "Pés"),
        ItemDefesa("Botas Flamejantes", "Equipamento", 5, 10, "Pés"),

    ]

    return choice(itens_possiveis)




