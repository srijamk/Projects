import random
class Coin():

    def coin_flipper(self):

        if random.randint(1, 2) == 1:
            return "Heads"
        else:
            return "Tails"


    def play(self):

        print "%s!" % self.coin_flipper()
        again = raw_input("Press Enter to play another trial. ")

    def coin_simulator(self, player1, player2):
        player_counter = 0
        player1_wins = 0
        player2_wins = 0
        print "Hello %s and %s. %s, you will get heads." % (player1, player2, player1)
        print "Let the game begin, then!"
        print "%s!" % self.coin_flipper()
        if self.coin_flipper() == "Heads":
            player1_wins += 1
        elif self.coin_flipper() == "Tails":
            player2_wins += 1
        again = raw_input("Press Enter to play another trial. ")
        while again == "" and player_counter <= 10:
            player_counter += 1
            self.play()
        return player1_wins, player2_wins


print Coin().coin_simulator("Srija", "Varsha")
