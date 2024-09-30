from objects.obj import Boneco, Item

player = Boneco("\033[32mPLAYER\033[0m", "Guerreiro", 1, 0, 1000, 15, 15)
inimigo = Boneco("\033[31mINIMIGO\033[0m", "Guerreiro", 1, 0, 1000, 15, 15)

espada = Item("Espada", 50, 0)
punho = Item("Punho", 5,0)
escudo = Item("Escudo", 0,15)

player.equipar_item(espada)
player.equipar_item(espada)
inimigo.equipar_item(punho)

print("\n\033[32m--- Player ---\033[0m")
player.show_atr()

print("\n\033[31m--- Inimigo ---\033[0m")
inimigo.show_atr()

while player.vida > 0 and inimigo.vida > 0:
    acao = input("Você deseja \033[31matacar\033[0m? (s/n): ").strip().lower()

    if acao == 's':
        player.atacar(inimigo)
    else:
        print(f"{player.nome} decidiu não atacar.")

    if inimigo.vida > 0:
        inimigo.atacar(player)

if player.vida > 0:
    print(f"{player.nome} venceu a batalha!")
else:
    print(f"{inimigo.nome} venceu a batalha!")
