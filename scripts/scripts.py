from objects.obj import Boneco, Item

player = Boneco("Russo", "Guerreiro", 1, 0, 1000, 15)
inimigo = Boneco("Goblin", "Guerreiro", 1, 0, 1000, 15)

espada = Item("Espada", 50)
punho = Item("Punho", 5)

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
