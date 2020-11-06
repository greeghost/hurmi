cartes_couleurs = list(range(1, 15))
cartes_atout = list(range(0, 22))
couleurs = ['P', 'C', 'K', 'T', 'A']

def height_to_string(n):
    if n == 1:
        return 'As'
    if n == 11:
        return 'Valet'
    elif n == 12:
        return 'Cavalier'
    elif n == 13:
        return 'Dame'
    elif n == 14:
        return 'Roi'
    return str(n)
def color_to_string(c):
    if c == 'P':
        return 'Pique'
    if c == 'C':
        return 'Coeur'
    if c == 'K':
        return 'Carreau'
    if c == 'T':
        return 'Trèfle'
    return 'Atout'

class Carte():
    def __init__(self, height, suit):
        assert ((suit == 'A') and (height in cartes_atout)) or ((suit in couleurs[:-1]) and height in cartes_couleurs), "Invalid Combination"

        self.height = height
        self.suit = suit
        self.oudler = (self.suit == 'A') and (self.height in (0, 1, 21))

    def points(self):
        if self.oudler:
            return 4.5
        elif (self.height >= 11) and (self.suit != 'A'):
            return self.height - 9.5
        else:
            return .5

    def __lt__(self, other):
        suits = 'KTCPA'
        if suits.index(self.suit) < suits.index(other.suit):
            return True
        if suits.index(self.suit) > suits.index(other.suit):
            return False
        if self.height < other.height:
            return True
        return False

    def __eq__(self, other):
        return (self.suit == other.suit) and (self.height == other.height)

    def __str__(self):
        if self.oudler:
            if self.height == 0:
                return 'Excuse'
            elif self.height == 1:
                return 'Petit'
            else:
                return 'Vingt et un'
        if self.suit == 'A':
            return f"{self.height} d'Atout"
        if self.suit in "PT":
            return f"\033[100m{height_to_string(self.height)} de {color_to_string(self.suit)}\033[0m"
        return f"\033[101m{height_to_string(self.height)} de {color_to_string(self.suit)}\033[0m"

card_list = sorted([Carte(h, s) for h in cartes_couleurs for s in couleurs[:-1]] + [Carte(h, 'A') for h in cartes_atout], reverse = True)
