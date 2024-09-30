class Inimigos_animais:


    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu \033[32m{dano:.2f}\033[m de dano e agora tem \033[31m{self.vida:.2f}\033[m de vida.")


def inimigos_animais_disp():
    from random import choice

    inimigos_disponiveis = [
        Inimigos_animais("Aranha", 15, 5),
        Inimigos_animais("Rato", 10, 3),
        Inimigos_animais("Escorpião", 15, 10),
        Inimigos_animais("Lobo", 20, 10),
        Inimigos_animais("Urso", 30, 15),
        Inimigos_animais("Cobra", 12, 8),
        Inimigos_animais("Águia", 18, 7),
        Inimigos_animais("Javali", 25, 12),
        Inimigos_animais("Leão", 35, 18),
        Inimigos_animais("Tigre", 40, 20),
        Inimigos_animais("Crocodilo", 45, 22),
        Inimigos_animais("Gorila", 50, 15),
        Inimigos_animais("Rinoceronte", 60, 25),
        Inimigos_animais("Morcego", 10, 4),
        Inimigos_animais("Centopeia Gigante", 20, 6),
        Inimigos_animais("Hiena", 22, 9),
        Inimigos_animais("Lobo Alfa", 35, 15),
        Inimigos_animais("Elefante", 70, 30),
        Inimigos_animais("Falcão", 17, 6),
        Inimigos_animais("Canguru", 28, 13),
        Inimigos_animais("Tubarão", 50, 20),
        Inimigos_animais("Hipopótamo", 55, 25),
        Inimigos_animais("Dragão de Komodo", 38, 18),
        Inimigos_animais("Caranguejo Gigante", 20, 10)
    ]

    return choice(inimigos_disponiveis)