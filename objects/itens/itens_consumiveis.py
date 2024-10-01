class ItemConsumivel:
    def __init__(self, nome, tipo, dano=0, usabilidade=None, tam_pot=None):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.usabilidade = usabilidade

        if self.usabilidade == "pot_vida":

            if tam_pot == "Grande":
                self.cura = 35

            elif tam_pot == "Média":
                self.cura = 25

            elif tam_pot == "Pequena":
                self.cura = 15



def itens_disp_consumiveis():

    from random import choice
    itens_possiveis = [
        ItemConsumivel("Poção de Vida Pequena", "Consumível", usabilidade="pot_vida", tam_pot='Pequena'),
        ItemConsumivel("Poção de Vida Grande", "Consumível", usabilidade="pot_vida", tam_pot="Grande"),
        ItemConsumivel("Poção de Vida Média", "Consumível", usabilidade="pot_vida", tam_pot="Média")
    ]

    return choice(itens_possiveis)
