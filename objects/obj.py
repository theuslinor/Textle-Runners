# objects/obj.py

class Item:
    def __init__(self, nome, dano, defesa):
        self.nome = nome
        self.dano = dano
        self.defesa = defesa

class Boneco:
    def __init__(self, nome, classe, nivel, xp, vida, defesa, d_Atk):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.xp = xp
        self.vida = vida
        self.defesa = defesa
        self.d_Atk = d_Atk
        self.item = None

    def show_atr(self):
        print(f"Nome: {self.nome}\n"
              f"Classe: {self.classe}\n"
              f"Nível: {self.nivel}\n"
              f"XP: {self.xp}\n"
              f"Vida: {self.vida}\n"
              f"Defesa: {self.defesa}\n"
              f"Dano de Ataque: {self.d_Atk}\n"
              f"Item Equipado: {self.item.nome if self.item else 'Nenhum'}")

    def equipar_item(self, item):
        self.item = item

    def atacar(self, outro):
        global dano_total
        dano_item = self.item.dano if self.item else 0
        dano_total = (dano_item * (self.d_Atk / 100)) + dano_item
        print(f"\n{self.nome} ataca {outro.nome} causando {dano_total:.1f} de \033[31mdano\033[0m!\n")
        outro.receber_dano(dano_total)

    def receber_dano(self, dano):
        reducao_defesa = dano * (self.defesa / 100)
        dano_recebido = dano - reducao_defesa
        if dano_recebido < 0:
            dano_recebido = 0
        self.vida -= dano_recebido
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano_recebido:.1f} de \033[31mdano\033[0m e agora tem {self.vida:.1f} de \033[32mvida\033[0m.")


