sum_num = 0

for x in range(5):
  if x % 3 == 0 or x % 5 == 0 or x % 3 == 0 and x % 5 == 0:
    sum_num += x
print sum_num
