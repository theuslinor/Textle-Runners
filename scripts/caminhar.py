import random

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

class Item:
    def __init__(self, nome, tipo, dano=0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano

class Boneco:

    def __init__(self, nome, forca, nivel=0, arma=None):
        self.vida  = 100
        self.nivel = nivel
        self.nome = nome
        self.movimento = False
        self.qtd_passos = 0
        self.inventario = []
        self.inimigo_encontro = None
        self.arma = arma
        self.forca = forca


    def show_player(self):
        if self.nivel == 0:
            print(f"Você, {self.nome}, um intrépido aventureiro, se prepara para desbravar as trevas da masmorra ancestral.\n"
                  f"Com seu inventário em mãos, você carrega itens que podem mudar o rumo da sua jornada.\n" 
                  f"Enquanto o eco dos seus passos ressoa nas paredes frias, o cheiro de aventuras e perigos paira no ar.\n"
                  f"Seus desafios começam agora: criaturas ferozes, armadilhas astutas e enigmas enigmáticos esperam por você\n"
                  f"nas sombras. Lembre-se, cada item do seu inventário pode ser a chave para a sobrevivência!\n"
                  f"Prepare-se para escrever sua própria lenda. Amasse seus medos, pois a aventura aguarda!\n")


        if len(self.inventario) < 1:
            print(f"Você possui ZERO itens no seu inventário, boa sorte em sua nova aventura!\n\n")
        else:
            print(f"Você possui {len(self.inventario)} itens no inventário, deseja equipar algum?")


    def atacar(self, inimigo):
        if self.arma:
            dano_item = self.arma.dano if self.arma else 0
            dano_total = (dano_item * (self.forca / 100)) + dano_item
            print(f"{self.nome} ataca {inimigo.nome} causando {dano_total:.2f} de dano!")
            inimigo.receber_dano(dano_total)
        else:
            self.receber_dano(inimigo.dano)


    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu \033[32m{dano:.2f}\033[m de dano e agora tem \033[31m{self.vida:.2f}\033[m de vida.")

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
            inimigo_encontrado = inimigos_animais_disp()
            mensagem = self.set_inimigo(inimigo_encontrado)
            print(mensagem)
            escolha = input("Lutar ou Fugir? (S/N) S = Lutar / N = Fugir: ").upper()
            while escolha not in ['S', 'N']:
                escolha = input("Lutar ou Fugir? (S/N) S = Lutar / N = Fugir: ").upper()
            if escolha == "S":
                self.inimigo_encontro = True
                while self.inimigo_encontro:
                    self.atacar(inimigo_encontrado)
                    if inimigo_encontrado.vida > 1:
                        self.receber_dano(inimigo_encontrado.dano)
                        if self.vida < 1:
                            print("Você perdeu!")
                            creditos()
                            exit()
                    elif inimigo_encontrado.vida < 1:
                        resp = 3
                        while resp not in [1, 2]:
                            resp = input(f"{inimigo_encontrado.nome} DERROTADO!\n"
                                         f"Deseja equipar algum item ou continuar sua exploração?\n"
                                         f"Equipar = 1 | Continuar 2\n"
                                         f"Faça sua escolha com base nos numeros demonstrados")
                        if resp == 1:
                            self.equipar_arma()

                        self.inimigo_encontrado = False

                else:
                    chance = random.randint(0, 100)
                    if chance < 20:
                        print("Escapou com sucesso!")

                    else:
                        self.atacar(inimigo_encontrado)

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
        Item("Galaxy Note 7", "Arma", dano=25),
        Item("Poção de Vida", "Consumível"),
        Item("Espada Curta", "Arma", dano=10),
        Item("Espada Longa", "Arma", dano=15),
        Item("Machado de Batalha", "Arma", dano=20),
        Item("Elixir de Mana", "Consumível"),
        Item("Arco Curto", "Arma", dano=12),
        Item("Flechas Infinitas", "Acessório"),
        Item("Poção de Invisibilidade", "Consumível"),
        Item("Escudo de Bronze", "Defesa"),
        Item("Elmo de Aço", "Equipamento"),
        Item("Anel de Regeneração", "Acessório"),
        Item("Poção de Cura Rápida", "Consumível"),
        Item("Bastão de Magia", "Arma", dano=18),
        Item("Daga Envenenada", "Arma", dano=8),
        Item("Cota de Malha", "Defesa"),
        Item("Botas da Velocidade", "Equipamento"),
        Item("Chave do Cofre", "Especial"),
        Item("Espada Flamejante", "Arma", dano=25),
        Item("Livro de Magias", "Consumível"),
        Item("Poção de Resistência", "Consumível"),
        Item("Lança de Ouro", "Arma", dano=30),
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

def start():
    print('--- TEXTLE RUNNERS ---')
    print('')
    print('\t1 - NOVO JOGO')
    print('\t2 - CONTINUAR')
    print('\t3 - SAIR\n')
    print("----------------------")
    res = int(input('Digite o numero de acordo com as opções: '))
    while res not in [1, 2, 3]:
        res = int(input('Digite o numero de acordo com as opções: '))

    if res == 1:
        #criar_novo_jogo(input("Digite o nome do seu personagem: "))
        debug()
        debugger.show_player()
    if res == 2:
        carregar_jogo()
    if res == 3:
        creditos()
        exit()




def criar_novo_jogo(nome):
    global char
    char = Boneco(nome, 10, nivel=0)
    return char

def debug():
    global debugger
    debugger = Boneco("Kat", nivel=10, arma=Item("Galaxy Note 7", "Arma", dano=25), forca=10)


def carregar_jogo():
    #Criar logica para carregar o jogo
    pass


def creditos():
    print("\nJogo criado e desenvolvido por:\n"
          "\033[35mMatheus dos Santos - github.com/theuslinor\033[m\n"
          "\033[31mVinicius Oliveira - github.com/kat4r\033[m")

#----------------------------------------------
# O Jogo roda aqui
#----------------------------------------------

start()



for i in range(10):
    #char.caminhar()
    debugger.caminhar()
# Mostrar o inventário final
#char.equipar_arma()
#char.mostrar_inv()



