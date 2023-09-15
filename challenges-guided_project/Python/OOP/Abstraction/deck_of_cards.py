import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    # ?

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"


def test(deck):
    print(deck)
    print("Dealing a hand:")
    hand = []
    for i in range(5):
        card = deck.deal_card()
        if card is None:
            print("Out of cards!")
            break
        print(f" - {card[0]} of {card[1]}")
    print("=====================================")
    return deck


def main():
    random.seed(1)
    deck = DeckOfCards()
    deck.shuffle_deck()
    deck = test(deck)
    deck = test(deck)
    deck = test(deck)


main()