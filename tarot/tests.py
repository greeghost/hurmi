from random import shuffle
import cards as c
import player as p

for name in ["Aaron", "Bruno", "Clara", "Danny", "Eliot"]:
    p.new_player(name)

p.deal(p.Player.player_list, c.card_list)

p.print_hands()
