def get_largest_palindromic_product():
    product_set = []
    for x in range(1, 1000):
        for y in range(1, 1000):
            if is_palindrome(x * y):
                product_set.append(x * y)
    return max(product_set)

def is_palindrome(num):
    num = list(str(num))
    new_num = []
    for i in reversed(num):
        new_num.append(i)
    return num == new_num

print get_largest_palindromic_product()

# Answer: 906609
