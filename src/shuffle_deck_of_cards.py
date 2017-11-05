import random

class Cards():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "K", "J", "Q", "A"]
    suits = ["s", "h", "d", "c"]
    def createDeck(self):
        deck = []
        for value in self.values:
            for suit in self.suits:
                deck.append(value + suit)
        return deck

    def shuffle(self):
        deck = self.createDeck()
        for index, card in enumerate(deck[0:-1]):
            random_number = random.randrange(index + 1, len(deck))
            deck[index], deck[random_number] = deck[random_number], deck[index]
        return deck

    def shuffle_numbers(self):
        lst = ["a", "b", "c", "d"]
        for index, num in enumerate(lst[0:-2]):
            random_index = random.randint(index + 1, len(lst))
            lst[index], lst[random_index] = lst[random_index], lst[index]
        return lst


if __name__ == '__main__':
    print "Original Deck: " + str(Cards().createDeck())
    print
    print "Shuffled Deck: " + str(Cards().shuffle())
