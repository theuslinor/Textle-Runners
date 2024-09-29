# objects/obj.py

class Item:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

class Boneco:
    def __init__(self, nome, classe, nivel, xp, vida, d_Atk):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.xp = xp
        self.vida = vida
        self.d_Atk = d_Atk
        self.item = None

    def show_atr(self):
        print(f"Nome: {self.nome}\n"
              f"Classe: {self.classe}\n"
              f"Nível: {self.nivel}\n"
              f"XP: {self.xp}\n"
              f"Vida: {self.vida}\n"
              f"Dano de Ataque: {self.d_Atk}\n"
              f"Item Equipado: {self.item.nome if self.item else 'Nenhum'}")

    def equipar_item(self, item):
        self.item = item

    def atacar(self, outro):
        dano_item = self.item.dano if self.item else 0
        dano_total = (dano_item * (self.d_Atk / 100)) + dano_item
        print(f"{self.nome} ataca {outro.nome} causando {dano_total:.2f} de dano!")
        outro.receber_dano(dano_total)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano:.2f} de dano e agora tem {self.vida:.2f} de vida.")
