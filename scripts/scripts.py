from objects.obj import Boneco, Item

player = Boneco("PLAYER", "Guerreiro", 1, 0, 1000, 15, 15)
inimigo = Boneco("INIMIGO", "Guerreiro", 1, 0, 1000, 15, 15)

espada = Item("Espada", 50, 0)
punho = Item("Punho", 5,0)
escudo = Item("Escudo", 0,15)

player.equipar_item(espada)
player.equipar_item(espada)
inimigo.equipar_item(punho)

player.show_atr()
print("\n--- Inimigo ---")
inimigo.show_atr()

while player.vida > 0 and inimigo.vida > 0:
    acao = input("Você deseja atacar? (s/n): ").strip().lower()

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
