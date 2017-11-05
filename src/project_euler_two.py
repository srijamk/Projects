def get_fibonacci(num):
    x = 1
    y = 2
    even_values = []
    fib_num = 0
    while y < num:
        if x % 2 == 0:
            even_values.append(x)
        x += y
        if y % 2 == 0:
            even_values.append(y)
        y += x

    return sum(even_values)


print get_fibonacci(4000000)

# Answer: 4,613,732
