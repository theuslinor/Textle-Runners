import sys
import os
import random
from objects.itens.itens_consumiveis import itens_disp_consumiveis
from objects.itens.itens_defesa import itens_disp_defesa

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from objects.itens.itens_dano_fisico import *
from objects.inimigos.inimigos_selvagens import *


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
        self.punhos = ItemDanoPhys("Punhos", "Arma", 500)

    def show_player(self):
        if self.nivel == 0:
            print(f"Você, {self.nome}, um intrépido aventureiro, se prepara para desbravar as trevas da masmorra ancestral.\n"
                  f"Com seu inventário em mãos, você carrega itens que podem mudar o rumo da sua jornada.\n" 
                  f"Enquanto o eco dos seus passos ressoa nas paredes frias, o cheiro de aventuras e perigos paira no ar.\n"
                  f"Seus desafios começam agora: criaturas ferozes, armadilhas astutas e enigmas enigmáticos esperam por você\n"
                  f"nas sombras. Lembre-se, cada item do seu inventário pode ser a chave para a sobrevivência!\n"
                  f"Prepare-se para escrever sua própria lenda. Amasse seus medos, pois a aventura aguarda!\n")

    def show_inventario(self):
        print(f"--- Inventário de {self.nome} ---")
        for pos, item in enumerate(self.inventario):
            print(f"\033[32m{pos+1}\033[m - \033[36m{item.nome}\033[m")
        if self.arma:
            print(f"Item equipado {self.arma.nome}")


    def curar_se(self,item):
        print(f"{item.nome} consumida!")
        self.vida += item.cura
        print(f"Você se curou em {item.cura}, vida: {self.vida}")

    def atacar(self, inimigo):
        if self.arma:
            dano_item = self.arma.dano if self.arma else 0
            dano_total = (dano_item * (self.forca / 100)) + dano_item
            print(f"{self.nome} ataca {inimigo.nome} causando {dano_total:.2f} de dano!")
            inimigo.receber_dano(dano_total)
        else:
            self.arma = self.punhos

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu \033[32m{dano:.2f}\033[m de dano e agora tem \033[31m{self.vida:.2f}\033[m de vida.")

    def batalha(self, inimigo_encontrado):

        global frase_continuidade
        frase_continuidade = (f"Deseja equipar algum item ou continuar sua exploração?\n"
                              f"[ 1 ] - Equipar\n"
                              f"[ 2 ] - Continuar\n")

        modo = "frase"
        while modo not in ['S', 'N']:
            modo = input(
                "Deseja realizar a batalha por turnos? (S/N) S = Turn based battle | N = Modo Autobattle: ").upper()

        if modo == "S":
            self.inimigo_encontro = True
            while self.inimigo_encontro:
                # Combate por turnos
                print(f"\n{self.nome} vs {inimigo_encontrado.nome}")
                print(f"Sua vida: {self.vida} | Vida do inimigo: {inimigo_encontrado.vida}\n")

                # Prompt para o jogador escolher entre atacar ou usar um item
                escolha_turno = int(input("[ 1 ] Atacar\n"
                                          "[ 2 ] Usar item\n"
                                          "Escolha: "))

                while escolha_turno not in [1, 2]:
                    escolha_turno = int(input("Escolha inválida. O que deseja fazer?\n"
                                              "[ 1 ] Atacar\n"
                                              "[ 2 ] Usar item\n"
                                              "Escolha: "))

                if escolha_turno == 1:
                    self.atacar(inimigo_encontrado)
                    if inimigo_encontrado.vida > 0:
                        print(f"Você atacou o {inimigo_encontrado.nome}!")
                    else:
                        print(f"Você derrotou o {inimigo_encontrado.nome}!")
                        break
                if escolha_turno == 2:
                    self.show_inventario()

                # Verifica se o inimigo está vivo para contra-atacar
                if inimigo_encontrado.vida > 0:
                    self.receber_dano(inimigo_encontrado.dano)
                    if self.vida > 0:
                        print(f"O {inimigo_encontrado.nome} te atacou! Sua vida atual: {self.vida}")
                    else:
                        print("Você foi derrotado!")
                        creditos()
                        exit()

            # Derrota do inimigo
            if inimigo_encontrado.vida <= 0:


                resp = 3
                while resp not in [1, 2]:
                    print(f"{inimigo_encontrado.nome} DERROTADO!\n")
                    resp = int(input(frase_continuidade))
                if resp == 1:
                    self.show_inventario()

        else:
            # Modo Autobattle
            while inimigo_encontrado.vida > 0 and self.vida > 0:
                self.atacar(inimigo_encontrado)
                if inimigo_encontrado.vida > 0:
                    self.receber_dano(inimigo_encontrado.dano)
                if self.vida <= 0:
                    print("Você foi derrotado!")
                    creditos()
                    exit()

            if inimigo_encontrado.vida <= 0:
                print(f"{inimigo_encontrado.nome} foi derrotado!")
                resp = 3
                while resp not in [1, 2]:
                    resp = int(input(frase_continuidade))
                if resp == 1:
                    self.show_inventario()
                    self.equipar_arma()

    def caminhar(self):
        # Checar chance de encontrar um item
        if random.randint(0, 100) < 50:

            item_encontrado = random.choice([itens_disp_dano_fisico(), itens_disp_defesa(), itens_disp_consumiveis()])
            mensagem = self.set_item(item_encontrado)
            print(mensagem)  # Agora imprime a mensagem de item encontrado

        else:
            inimigo_encontrado = inimigos_animais_disp()
            mensagem = self.set_inimigo(inimigo_encontrado)
            print(mensagem)
            print(self.self_insert())
            escolha = "frase"
            while escolha not in ['S', 'N']:
                escolha = input("Lutar ou Fugir? (S/N) S = Lutar / N = Fugir: ").upper()

            if escolha == "S":
                self.batalha(inimigo_encontrado)
            else:
                chance = random.randint(0, 100)
                if chance < 20:
                    print("Você escapou com sucesso!")
                else:
                    print("Você falhou em escapar!")
                    self.receber_dano(inimigo_encontrado.dano)
                    self.batalha(inimigo_encontrado)

        self.qtd_passos += 1

    def equipar_arma(self):
        if len(self.inventario) < 1:
            print(f"Você não possui itens para equipar")
        else:
            resposta = 15
            while resposta >= len(self.inventario):  # Corrigido para garantir que o índice está dentro do limite
                print(f"Tamanho do inventário: {len(self.inventario)}")
                print("Item não encontrado, verifique o número utilizado")
                resposta = int(input("Qual item deseja equipar? [Escolha de acordo com o número indicado acima]: ")) - 1

                # Verifica se o item existe e se é consumível
                if self.inventario[resposta] and self.inventario[resposta].tipo == "Consumível":
                    # Executa a cura antes de remover o item
                    self.curar_se(self.inventario[resposta])  # Utiliza o item atual
                    self.inventario.pop(resposta)  # Agora remove o item consumível
                    break

                # Verifica se o item possui dano, ou seja, é uma arma
                elif self.inventario[resposta].dano > 0:
                    self.arma = self.inventario[resposta]
                    print(f"Você equipou {self.arma.nome}")

    def set_item(self, item):
        self.inventario.append(item)
        return f"{self.nome} encontrou um {item.nome}!"

    def set_inimigo(self, inimigo):
        self.inimigo_encontro = inimigo
        return (f"{self.nome} encontrou um {inimigo.nome}!\n\n"
                f"--- Status de \033[31m{inimigo.nome}\033[m ---\n"
                f"\033[32mVida\033[0m: {inimigo.vida}\n"
                f"\033[34mDano\033[m: {inimigo.dano}\n")

    def self_insert(self):
        if not self.arma:
            self.arma = self.punhos
        return (f"--- Status de \033[35m{self.nome}\033[m ---\n"
                f"\033[32mVida\033[0m: {self.vida}\n"
                f"\033[34mDano\033[m: {(self.arma.dano * (self.forca / 100)) + self.arma.dano}\n" 
                f"\033[36mArma equipada:\033[m {self.arma.nome}\n")


def start():

    while True:

        try:

            print('---- \033[30;47mTEXTLE RUNNERS\033[m ----')
            print('-                      -')
            print('-  [ 1 ] - NOVO JOGO   -')
            print('-  [ 2 ] - CONTINUAR   -')
            print('-  [ 3 ] - SAIR        -')
            print('-  [ 4 ] - MANUAL      -')
            print("------------------------")
            res = int(input('Digite o numero de acordo com as opções: '))
            while res not in [1, 2, 3, 4]:
                res = int(input('Digite o numero de acordo com as opções: '))

            if res == 1:
                criar_novo_jogo(input("Digite o nome do seu personagem: "))
                #debug()
                #debugger.show_player()
                gameloop()
            if res == 2:
                carregar_jogo()
                gameloop()
            if res == 3:
                creditos()
                exit()
            if res == 4:
                print(f"\n\tBem vindo à Textle Runners!\n"
                      f"\tUm rpg de turnos baseado em texto\n\n"
                      f"----------- COMO JOGAR -----------\n"
                      f"1 - Ao iniciar o jogo será primeiro perguntado o nome de seu aventureiro\n"
                      f"2 - Até o momento somente o NOME é escolha do jogador\n"
                      f"3 - O gameplay loop envolve caminhar e fazer algum encontro aleatório.\n"
                      f"O encontro pode ser um inimigo ou então um item, que será pego aumaticamente e guardado em seu inventário.\n"
                      f"A cada rodada você terá a escolha de utilizar de seu inventário ou então de continuar a caminhar.\n"
                      f"\t\t    DIVIRTA-SE")
                start() if input("pressione ENTER para continuar: ") else start()

        except Exception as erro:

            print("Erro ao iniciar o jogo! Vamos tentar novamente.")
            print(f"Erro encontrado {erro}")
            continue


def gameloop():
    char.show_player()

    print(f"Sua jornada começa aqui\n")
    while True:

        print(f"Passos atuais: {char.qtd_passos}\n"
              f"O que deseja fazer?\n"
              f"[ 1 ] - Caminhar\n"
              f"[ 2 ] - Checar inventário\n"
              f"[ 3 ] - Sair\n")

        resp = 0
        while resp not in [1, 2, 3]:
            resp = int(input("Digite o número de acordo com sua escolha: "))
        if resp == 1:
            char.caminhar()

        elif resp == 2:
            char.show_inventario()
            equip = input("Deseja equipar algo? [ S / N ]: ").upper()
            while equip not in ['S', 'N']:
                equip = input("Deseja equipar algo? [ S / N ]: ").upper()
            if equip == 'S':
                char.equipar_arma()
            else:
                continue
        elif resp == 3:
            creditos()
            exit()



def criar_novo_jogo(nome):
    global char
    char = Boneco(nome, 10, nivel=0)
    return char

def debug():
    global debugger
    debugger = Boneco("Kat", nivel=10, arma=ItemDanoPhys("Galaxy Note 7", "Arma", dano=25), forca=10)

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
