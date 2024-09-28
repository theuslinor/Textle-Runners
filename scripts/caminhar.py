import random

class Inimigos_animais:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo


class Boneco:

    def __init__(self, nome):
        self.nome = nome
        self.movimento = False
        self.qtd_passos = 0
        self.inventario = []
        self.inimigo_encontro = None
        self.arma = None

    def caminhar(self):
        # Simular o movimento a cada chamada
        self.movimento = True
        self.qtd_passos += 1
        print(f"{self.nome} deu um passo. Total de passos: {self.qtd_passos}")

        # Checar chance de encontrar um item
        if random.randint(0, 100) < 50:
            item_encontrado = itens_disp()
            mensagem = self.set_item(item_encontrado)
            print(mensagem)  # Agora imprime a mensagem de item encontrado
        else:
            inimigo_encontrando = inimigos_animais_disp()
            mensagem = self.set_inimigo(inimigo_encontrando)
            print(mensagem, )
            escolha = input("Lutar ou Fugir? (S/N) S = Lutar / N = Fugir: ")
            while escolha not in ['S', 'N']:
                if escolha == "S":
                    pass
                else:
                    chance = random.randint(0, 100)
                    if chance < 20:
                        print("Escapou com sucesso!")
                        break
                    else:
                        pass
        self.movimento = False  # Resetar o estado de movimento após a ação

    def equipar_arma(self):
        if not self.arma:
            if len(self.inventario) < 1:
                print(f"Você não possui itens para equipar")
            for pos, item in enumerate(self.inventario):
                print(f"{pos+1} - {item.nome}")
            resposta = int(input("Qual item deseja equipar? [Escolha de acordo com o numero indicado acima]: "))-1
            while resposta > len(self.inventario):
                print(f"tamanho do inventário: {len(self.inventario)}")
                print("Item não encontrado, verifique o número utilizado")
                resposta = int(input("Qual item deseja equipar? [Escolha de acordo com o numero indicado acima]: "))-1
            self.arma = self.inventario[resposta].nome
            print(f"Você equipou {self.arma}")


    def set_item(self, item):
        self.inventario.append(item)
        return f"{self.nome} encontrou um {item.nome}!"

    def set_inimigo(self, inimigo):
        self.inimigo_encontro = inimigo
        return (f"{self.nome} encontrou um {inimigo.nome}!\n\n"
                f"--- Status de \033[31m{inimigo.nome}\033[m ---\n"
                f"\033[32mVida\033[0m: {inimigo.vida}\n"
                f"\033[34mDano\033[m: {inimigo.dano}\n")

    def mostrar_inv(self):
        print(f"--- Inventário de {self.nome} ---")
        for pos, item in enumerate(self.inventario):
            print(f"\033[32m{pos+1}\033[m - \033[36m{item.nome}\033[m")
        if self.arma:
            print(f"Item equipado {item.nome}")


def itens_disp():
    itens_possiveis = [
        Item("Galaxy Note 7", "Arma"),
        Item("Poção de Vida", "Consumível"),
        Item("Espada Curta", "Arma"),
        Item("Espada Longa", "Arma"),
        Item("Machado de Batalha", "Arma"),
        Item("Elixir de Mana", "Consumível"),
        Item("Arco Curto", "Arma"),
        Item("Flechas Infinitas", "Acessório"),
        Item("Poção de Invisibilidade", "Consumível"),
        Item("Escudo de Bronze", "Defesa"),
        Item("Elmo de Aço", "Equipamento"),
        Item("Anel de Regeneração", "Acessório"),
        Item("Poção de Cura Rápida", "Consumível"),
        Item("Bastão de Magia", "Arma"),
        Item("Daga Envenenada", "Arma"),
        Item("Cota de Malha", "Defesa"),
        Item("Botas da Velocidade", "Equipamento"),
        Item("Chave do Cofre", "Especial"),
        Item("Espada Flamejante", "Arma"),
        Item("Livro de Magias", "Consumível"),
        Item("Poção de Resistência", "Consumível"),
        Item("Lança de Ouro", "Arma"),
        Item("Escudo de Cristal", "Defesa"),
        Item("Armadura de Dragão", "Equipamento"),
        Item("Amuleto da Sorte", "Acessório")
    ]
    return random.choice(itens_possiveis)

def inimigos_animais_disp():
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

    return random.choice(inimigos_disponiveis)

# Criar o boneco e simular movimento
p1 = Boneco('player')

for i in range(10):
    p1.caminhar()

# Mostrar o inventário final
p1.equipar_arma()
p1.mostrar_inv()

