import sys
import random
import time

class GamblerRuin():
  def gambler_ruin(self, stake, goal, num_games):
    start = time.time()
    games = num_games
    bets = 0
    wins = 0
    print
    while games > 0:
      cash = stake

      while cash > 0 and cash < goal:
        if random.random() >= 0.5:
          cash += 1
        else:
          cash -= 1
        bets += 1
 
      if cash == goal:
        wins += 1
      games -= 1
    end = time.time()
    elapsed = end - start
    print "Time: " + str(elapsed)
    average_bets = bets / num_games
    percent_wins = (wins / (num_games * 1.0)) * 100
    return "Average Bets: " + str(average_bets) + ", Percentage of Wins: " + str(percent_wins) + "%"



if __name__ == '__main__':
  if len(sys.argv) != 4:
    stake, goal, num_games = raw_input("Please enter four parameters: ").split( )
  else:
    stake = sys.argv[1]
    goal = sys.argv[2]
    num_games = sys.argv[3]

  num = GamblerRuin()
  print num.gambler_ruin(int(stake), int(goal), int(num_games))
