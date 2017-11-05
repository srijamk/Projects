f = [1, 2]
x = 0
y = 1
sum_num = 0
while len(f) < 4000000:
  f.append(f[x] + f[y])
  x += 1
  y += 1
even_values = []
for item in f:
  if item % 2 == 0:
    even_values.append(item)
for item in even_values:
  sum_num += item
print sum_num
