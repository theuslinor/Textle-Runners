class Inimigos_animais:


    def __init__(self, nome, vida, dano, chance_escape):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.chance_escape = chance_escape
        self.vida_maxima = self.vida


    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu \033[32m{dano:.2f}\033[m de dano e agora tem \033[31m{self.vida:.2f}\033[m de vida.")


def inimigos_animais_disp():
    from random import choice

    inimigos_disponiveis = [
        Inimigos_animais("Aranha", 15, 5, 80),
        Inimigos_animais("Rato", 10, 3, 90),
        Inimigos_animais("Escorpião", 15, 10, 75),
        Inimigos_animais("Lobo", 20, 10, 35),
        Inimigos_animais("Urso", 30, 15, 40),
        Inimigos_animais("Cobra", 12, 8, 85),
        Inimigos_animais("Águia", 18, 7, 20),
        Inimigos_animais("Javali", 25, 12, 40),
        Inimigos_animais("Leão", 35, 18, 30),
        Inimigos_animais("Tigre", 40, 20, 15),
        Inimigos_animais("Crocodilo", 45, 22, 30),
        Inimigos_animais("Gorila", 50, 15, 35),
        Inimigos_animais("Rinoceronte", 60, 25, 15),
        Inimigos_animais("Morcego", 10, 4, 90),
        Inimigos_animais("Centopeia Gigante", 20, 6, 70),
        Inimigos_animais("Hiena", 22, 9, 50),
        Inimigos_animais("Lobo Alfa", 35, 15, 30),
        Inimigos_animais("Elefante", 70, 30, 40),
        Inimigos_animais("Falcão", 17, 6, 20),
        Inimigos_animais("Canguru", 28, 13, 55),
        Inimigos_animais("Tubarão", 50, 20, 20),
        Inimigos_animais("Hipopótamo", 55, 25, 15),
        Inimigos_animais("Dragão de Komodo", 38, 18, 30),
        Inimigos_animais("Caranguejo Gigante", 20, 10, 75)
    ]

    return choice(inimigos_disponiveis)