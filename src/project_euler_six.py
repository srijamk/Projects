def sum_square_difference():
    square_sum = 0
    for x in range(101):
        square_sum += x ** 2
    return abs(square_sum - sum(range(101)) ** 2)

print sum_square_difference()

# Result: 25840850
