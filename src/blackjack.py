import random
card_values = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
card_1 = random.choice(card_values)
card_2 = random.choice(card_values)
if card_1 == "A":
    card_1 = "1"
elif card_2 == "A":
    card_1 = "1"

print card_1
print card_2

card_total = int(card_1) + int(card_2)

first_hit_or_stand = raw_input("Your card total is " + str(card_total) + ". Would you like to hit or stand? ")

if first_hit_or_stand == "hit":
    new_card = random.choice(card_values)
    if new_card == "A" and card_total + 11 <= 21:
        new_card = 11
    elif new_card == "A" and card_total + 11 > 21:
        new_card = 1
    card_total += int(new_card)

    if card_total > 21:
        print "You busted! You lose! Play again? "

    elif card_total < 21:
        second = raw_input("Nice! You didn't bust! Your card total is now " + str(card_total) + ". Would you like to hit or stand? ")

        if second == "hit":
            new_card = random.choice(card_values)
            if new_card == "A" and card_total + 11 <= 21:
                new_card = 11
            elif new_card == "A" and card_total + 11 > 21:
                new_card = 1
            card_total += int(new_card)

            if card_total > 21:
                print "You busted! You lose! Play again? "
            if card_total < 21:
                third = raw_input("Nice! You didn't bust! Your card total is now " + str(card_total) + ". Would you like to hit or stand? ")
                if third == "hit":
                    new_card = random.choice(card_values)
                    if new_card == "A" and card_total + 11 <= 21:
                        new_card = 11
                    elif new_card == "A" and card_total + 11 > 21:
                        new_card = 1

                    card_total += int(new_card)

                    if card_total > 21:
                        print "You busted! You lose! Play again? "
                    elif card_total < 21:
                        fourth = raw_input("Nice! You didn't bust! Your card total is now " + str(card_total) + ". Would you like to hit or stand? ")
                        if fourth == "hit":
                            new_card = random.choice(card_values)
                            if new_card == "A" and card_total + 11 <= 21:
                                new_card = 11
                            elif new_card == "A" and card_total + 11 > 21:
                                new_card = 1

                            card_total += int(new_card)

                            if card_total > 21:
                                print "You busted! You lose! Play again? "
                            elif card_total < 21:
                                fifth = raw_input("Nice! You didn't bust! Your card total is now " + str(card_total) + ". Would you like to hit or stand? ")
                                if fifth == "hit":
                                    new_card = random.choice(card_values)
                                    if new_card == "A" and card_total + 11 <= 21:
                                        new_card = 11
                                    elif new_card == "A" and card_total + 11 > 21:
                                        new_card = 1

                                    card_total += int(new_card)

                                    if card_total > 21:
                                        print "You busted! You lose! Play again? "
                                    elif card_total < 21:
                                        print "You stayed for this long! You win!"
                        elif fourth == "stand":
                            dealer_card_1 = random.choice(card_values)
                            dealer_card_2 = random.choice(card_values)

                            if dealer_card_1 == "A" and dealer_card_total + 11 <= 21:
                                dealer_card_1 = 11
                            elif dealer_card_1 == "A" and dealer_card_total + 11 > 21:
                                dealer_card_1 = 1
                            elif dealer_card_2 == "A" and dealer_card_total + 11 <= 21:
                                dealer_card_2 = 11
                            elif dealer_card_2 == "A" and dealer_card_total + 11 > 21:
                                dealer_card_2 = 1
                            dealer_card_total = int(dealer_card_1) + int(dealer_card_2)

                            if dealer_card_total == 21:
                                print "Aw, you lose because the dealer hit 21, too. Play again? "
                            elif dealer_card_total > 21:
                                print "You win! The dealer busted! "
                            else:
                                print "You win! You have a higher card total! "

                    else:
                        print "Awesome! You hit 21 exactly! You must stand."
                        dealer_card_1 = int(random.choice(card_values))
                        dealer_card_2 = int(random.choice(card_values))
                        dealer_card_total = dealer_card_1 + dealer_card_2

                        if dealer_card_total == 21:
                            print "Aw, you lose because the dealer hit 21, too. Play again? "
                        elif dealer_card_total > 21:
                            print "You win! The dealer busted!"
                        else:
                            print "You win! You have a higher card total!"


                elif third == "stand":
                    dealer_card_1 = random.choice(card_values)
                    dealer_card_2 = random.choice(card_values)

                    if dealer_card_1 == "A" and dealer_card_total + 11 <= 21:
                        dealer_card_1 = 11
                    elif dealer_card_1 == "A" and dealer_card_total + 11 > 21:
                        dealer_card_1 = 1
                    elif dealer_card_2 == "A" and dealer_card_total + 11 <= 21:
                        dealer_card_2 = 11
                    elif dealer_card_2 == "A" and dealer_card_total + 11 > 21:
                        dealer_card_2 = 1
                    dealer_card_total = int(dealer_card_1) + int(dealer_card_2)

                    if dealer_card_total == 21:
                        print "Aw, you lose because the dealer hit 21, too. Play again? "
                    elif dealer_card_total > 21:
                        print "You win! The dealer busted! "
                    else:
                        print "You win! You have a higher card total! "

            else:
                print "Awesome! You hit 21 exactly! You must stand."
                dealer_card_1 = int(random.choice(card_values))
                dealer_card_2 = int(random.choice(card_values))
                dealer_card_total = dealer_card_1 + dealer_card_2

                if dealer_card_total == 21:
                    print "Aw, you lose because the dealer hit 21, too. Play again? "
                elif dealer_card_total > 21:
                    print "You win! The dealer busted!"
                else:
                    print "You win! You have a higher card total!"

        elif second == "stand":
            dealer_card_1 = random.choice(card_values)
            dealer_card_2 = random.choice(card_values)
            if dealer_card_1 == "A" and int(dealer_card_2) + 11 <= 21:
                dealer_card_1 = 11
            elif dealer_card_1 == "A" and int(dealer_card_2) + 11 > 21:
                dealer_card_1 = 1
            elif dealer_card_2 == "A" and int(dealer_card_1) + 11 <= 21:
                dealer_card_2 = 11
            elif dealer_card_2 == "A" and int(dealer_card_1) + 11 > 21:
                dealer_card_2 = 1
            dealer_card_total = int(dealer_card_1) + int(dealer_card_2)

            print "Dealer Card Total is " + str(dealer_card_total)
            if dealer_card_total > card_total:
                print "Aw, you lose because the dealer had a higher card total. Play again? "
            elif dealer_card_total < card_total:
                print "You win! The dealer busted!"
            else:
                print "You win! You have a higher card total!"


    else:
        print "Awesome! You hit 21 exactly! You must stand."
        dealer_card_1 = random.choice(card_values)
        dealer_card_2 = random.choice(card_values)

        if dealer_card_1 == "A" and int(dealer_card_2) + 11 <= 21:
            dealer_card_1 = 11
        elif dealer_card_1 == "A" and int(dealer_card_2) + 11 > 21:
            dealer_card_1 = 1
        elif dealer_card_2 == "A" and int(dealer_card_1) + 11 <= 21:
            dealer_card_2 = 11
        elif dealer_card_2 == "A" and int(dealer_card_1) + 11 > 21:
            dealer_card_2 = 1
        dealer_card_total = int(dealer_card_1) + int(dealer_card_2)

        if dealer_card_total == 21:
            print "Aw, you lose because the dealer hit 21, too. Play again?"
        elif dealer_card_total > 21:
            print "You win! The dealer busted!"
        else:
            print "You win! You have a higher card total!"


if first_hit_or_stand == "stand":
    dealer_card_1 = random.choice(card_values)
    dealer_card_2 = random.choice(card_values)
    if dealer_card_1 == "A" and int(dealer_card_2) + 11 <= 21:
        dealer_card_1 = 11
    elif dealer_card_1 == "A" and int(dealer_card_2) + 11 > 21:
        dealer_card_1 = 1
    elif dealer_card_2 == "A" and int(dealer_card_1) + 11 <= 21:
        dealer_card_2 = 11
    elif dealer_card_2 == "A" and int(dealer_card_1) + 11 > 21:
        dealer_card_2 = 1
    dealer_card_total = int(dealer_card_1) + int(dealer_card_2)

    print "Dealer Card Total is " + str(dealer_card_total)
    if dealer_card_total > card_total:
        print "Aw, you lose because the dealer had a higher card total. Play again?"
    elif dealer_card_total < card_total:
        print "You win! The dealer busted!"
    else:
        print "You win! You have a higher card total!"
