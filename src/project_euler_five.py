def get_smallest_multiple():
    multiple = 4000
    while True:
        if multiple % 20 == 0 and multiple % 19 == 0 and multiple % 18 == 0 and multiple % 17 == 0 and multiple % 16 == 0 and multiple % 15 == 0 and multiple % 14 == 0 and multiple % 13 == 0 and multiple % 12 == 0 and multiple % 11 == 0 and multiple % 10 == 0 and multiple % 9 == 0 and multiple % 8 == 0 and multiple % 7 == 0 and multiple % 6 == 0 and multiple % 5 == 0 and multiple % 4 == 0 and multiple % 3 == 0 and multiple % 4 == 0 and multiple % 3 == 0 and multiple % 2 == 0 and multiple % 1 == 0:
            return multiple
            break
        multiple += 20

print get_smallest_multiple()

# Result: 232792560
