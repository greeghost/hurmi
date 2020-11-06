from random import shuffle

def get_player(name):
    for p in Player.player_list:
        if p.name == name:
            return p

class Player():
    player_list = []

    def __init__(self, name):
        Player.player_list.append(self)
        self.name = name
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)

def deal(player_list, card_list):
    shuffle(card_list)
    if len(player_list) == 5:
        chien = 3
    else:
        chien = 6
    i = chien
    chien = card_list[0:chien]
    while i < len(card_list):
        Player.player_list[i % len(player_list)].draw_card(card_list[i])
        i += 1
    if len(player_list) == 6:
        return chien[0:3], chien[3:6]
    else:
        return chien

if __name__ == '__main__':
    p1 = Player("Aaron")
    p2 = Player("Bruno")
    p3 = Player("Clara")
    p4 = Player("Danny")
    p5 = Player("Eliot")

    card_list = list(range(78))
    chien = deal(Player.player_list, card_list)
    for p in Player.player_list:
        print(p.name, ":", p.hand)
    print("chien :", chien)
