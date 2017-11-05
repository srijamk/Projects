class Total():
    def throw_one(self, total):
        total = total - 1
        return total

    def keep_share(self, total, n):
        total = total - (1 / n) * total
        return total

all_lsts = []
valid_nums = []
total = 0.0
n = 4.0
while total <= 150.0:

    all_lsts.append((str(Total().throw_one(total)), str(Total().keep_share(Total().throw_one(total), n))))
    total += 1

for tup in all_lsts:
    if tup[1][-1] == '0':
        valid_nums.append(tup)
valid_nums.pop(0)

for x in range(10):
    for index, tup in enumerate(valid_nums):
        valid_nums[index] += (str(Total().throw_one(eval(tup[-1]))), )

    for index, tup in enumerate(valid_nums):
        valid_nums[index] += (str(Total().keep_share(eval(tup[-1]), n)), )

for index, tup in enumerate(valid_nums):
    valid_nums[index] = list(tup)
    valid_nums[index].insert(0, str(eval(valid_nums[index][0]) + 1))
    if (eval(valid_nums[index][-1]) - 1.0) % n == 0:
        valid_nums[index] += (str(eval(valid_nums[index][-1]) - 1), )
for tup in valid_nums:
    print tup
