def get_multiples(num):
    multiples_list = []
    for x in range(1, num):
        if x % 3 == 0 or x % 5 == 0 or (x % 3 == 0 and x % 5 == 0):
            multiples_list.append(x)
    return sum(multiples_list)

print get_multiples(1000)

# Answer: 233,168
