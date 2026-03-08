# Flyttade från game.py

# Parameter score används i print_status och anropas i game.py. Värdet av score uppdateras varje gång funktionen anropas
def print_status(score, game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)