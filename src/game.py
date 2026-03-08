from .grid import Grid
from .player import Player
from . import pickups, status

# A. Spelaren ska börja nära mitten av rummet.
player = Player(int(Grid.width/2), int(Grid.height/2))
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)


# B. Förflyttningar i alla 4 riktningar. (Med tangenterna WASD.)
# Funktion för att undvika upprepa så mycket kod för riktningarna "W,A,S,D"
def move_player(dx, dy):
    global score, inventory # Behövs för att ändra på "score" och "inventory" variablerna som är deklarerad utanför funktionen

    # C. Man ska inte kunna gå igenom väggar.
    if not player.can_move(player.pos_x + dx, player.pos_y + dy, g):
        print("Du kan inte gå igenom väggar")
        return

    maybe_item = g.get(player.pos_x + dx, player.pos_y + dy)

    player.move(dx, dy)

    if isinstance(maybe_item, pickups.Item):
        # we found something
        score += maybe_item.value
        # E. Inventory - alla saker som man plockar upp ska sparas i en lista.
        inventory.append(maybe_item)
        print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
        # g.set(player.pos_x, player.pos_y, g.empty)
        g.clear(player.pos_x, player.pos_y)
    else:
        # G. The floor is lava - för varje steg man går ska man tappa 1 poäng.
        score -= 1

command = ""
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    status.print_status(score,g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    if command == "d":
        move_player(1, 0) # Höger
    elif command == "w":
        move_player(0, -1) # Upp
    elif command == "a":
        move_player(-1, 0) # Vänster
    elif command == "s":
        move_player(0, 1) # Ner
    # F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
    elif command == "i":
        if inventory:
            print("Inventory: ")
            for item in inventory:
                print(f"- {item.name}, value: {item.value}")
        else:
            print("Your inventory is empty.")


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")