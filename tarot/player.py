from random import shuffle

def new_player(name):
    return Player(name)

class Player():
    player_list = []

    def __init__(self, name):
        Player.player_list.append(self)
        self.name = name
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)

    def __str__(self):
        return self.name


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
    for player in Player.player_list:
        player.hand.sort(reverse = True)
    if len(player_list) == 6:
        return chien[0:3], chien[3:6]
    else:
        return chien


def print_hands():
    for player in Player.player_list:
        print(player.name)
        for card in player.hand:
            print(f"    {str(card)}")
