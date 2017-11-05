number = raw_input("Enter a number: ")
counter = 0.0
while number != "":
    try:
        counter += float(number)
        print counter
    except:
        print "Enter a number. "
    number = raw_input("Enter a number: ")
