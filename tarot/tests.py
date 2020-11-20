from random import shuffle

import cards as c
import player as p

for name in ["Aaron", "Bruno", "Clara", "Danny", "Eliot"]:
    p.new_player(name)


print("Chien :")

for card in p.deal(p.Player.player_list, c.card_list):
    print(f"    {str(card)}")

p.print_hands()

pl = p.Player.player_list[-1]
print(pl)
e.ask_move(pl)
