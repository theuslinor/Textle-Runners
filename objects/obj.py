class Boneco:

    def __init__(self, nome, classe, nivel, xp, vida, d_Atk):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.xp = xp
        self.vida = vida
        self.d_Atk = d_Atk
        self.acao = False


    def show_atr(self):
        print(f"Nome: {self.nome}\n"
              f"Classe: {self.classe}\n"
              f"Nível: {self.nivel}\n"
              f"XP: {self.xp}\n"
              f"Vida: {self.vida}\n"
              f"Dano de Ataque: {self.d_Atk}")

    def dano(self):
        if not self.acao:
            #dano de ataque hardcodded aqui \/
            self.vida = self.vida - 50
            return self.vida

