from shuffle_deck_of_cards import Cards
import random
class DealCards():
    def deal(self, num_of_hands, num_of_cards):
        deck = Cards().shuffle()
        all_dealed_hands = []
        for x in range(num_of_hands):
            new_hand = []
            for x in range(num_of_cards):
                new_card = random.randint(0, len(deck) - 1)
                new_hand.append(deck[new_card])
            all_dealed_hands.append(new_hand)
        return all_dealed_hands

num_of_hands = int(raw_input("Enter a number of hands: "))
num_of_cards = int(raw_input("Enter a number of cards: "))
print DealCards().deal(num_of_hands, num_of_cards)
