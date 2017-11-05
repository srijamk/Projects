number = raw_input("Press Enter to continue: ")
positives = []
negatives = []
zeroes = []
while number != "":
    number = raw_input("Enter a number: ")
    if number != "":
        if int(number) > 0:
            positives.append(int(number))
        elif int(number) < 0:
            negatives.append(int(number))
        else:
            zeroes.append(int(number))
    else:
        print negatives + zeroes + positives
