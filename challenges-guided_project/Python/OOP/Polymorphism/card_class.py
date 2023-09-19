# import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, card2): # card1.__eq__(card2)
        return RANKS.index(self.rank) == RANKS.index(card2.rank) and \
            SUITS.index(self.suit) == SUITS.index(card2.suit)

    def __gt__(self, card2): # card1.__gt__(card2)
        card1_rank = RANKS.index(self.rank)
        card2_rank = RANKS.index(card2.rank)
        card1_suit = SUITS.index(self.suit)
        card2_suit = SUITS.index(card2.suit)
        if card1_rank > card2_rank:
            return True
        elif card1_rank == card2_rank:
            if card1_suit > card2_suit:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, card2): # card1.__lt__(card2)
        card1_rank = RANKS.index(self.rank)
        card2_rank = RANKS.index(card2.rank)
        card1_suit = SUITS.index(self.suit)
        card2_suit = SUITS.index(card2.suit)
        if card1_rank < card2_rank:
            return True
        elif card1_rank == card2_rank:
            if card1_suit < card2_suit:
                return True
            else:
                return False
        else:
            return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"


def test(card1, card2):
    print(f"{card1} = {card2}: {card1 == card2}")
    print(f"{card1} > {card2}: {card1 > card2}")
    print(f"{card1} < {card2}: {card1 < card2}")
    print("------------------------------------------")


def main():
    test(Card("Ace", "Hearts"), Card("Queen", "Diamonds"))
    test(Card("2", "Spades"), Card("2", "Diamonds"))
    test(Card("King", "Hearts"), Card("Queen", "Diamonds"))
    test(Card("3", "Clubs"), Card("7", "Clubs"))
    test(Card("3", "Clubs"), Card("3", "Clubs"))

main()
