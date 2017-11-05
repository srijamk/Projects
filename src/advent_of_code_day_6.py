import re
with open ('advent_of_code_day_6_part_1_input.txt') as f:
    content = f.readlines()

all_lights = []
col = []
for x in range(0, 10):
    col.append(0)
for row in range(0, 10):
    all_lights.append(col)


def turn_on(tup1, tup2):
    for index, num in enumerate(all_lights):
        for index2, num2 in enumerate(num):
            if index >= tup1[0] and index <= tup2[0]:
                if index2 >= tup1[1] and index2 <= tup2[1]:
                    all_lights[index][index2] = 1


def toggle (tup1, tup2):
    for index, num in enumerate(all_lights):
        for index2, num2 in enumerate(num):
            if index >= tup1[0] and index <= tup2[0]:
                if index2 >= tup1[1] and index2 <= tup2[1]:
                    num = num[0:index2] + [1 - num2] + num[index2:num[len(num) - 1]]
                    all_lights = all_lights[]

def turn_off (tup1, tup2):
    for index, num in enumerate(all_lights):
        for index2, num2 in enumerate(num):
            if index >= tup1[0] and index <= tup2[0]:
                if index2 >= tup1[1] and index2 <= tup2[1]:
                    all_lights[index][index2] = 0
"""
for line in content:
    if line[0:6] == "toggle":
        toggle((int(re.findall('\d+', line)[0]), int(re.findall('\d+', line)[1])), (int(re.findall('\d+', line)[2]), int(re.findall('\d+', line)[3])))
    elif line[0:7] == "turn on":
        turn_on((int(re.findall('\d+', line)[0]), int(re.findall('\d+', line)[1])), (int(re.findall('\d+', line)[2]), int(re.findall('\d+', line)[3])))
    else:
        turn_off((int(re.findall('\d+', line)[0]), int(re.findall('\d+', line)[1])), (int(re.findall('\d+', line)[2]), int(re.findall('\d+', line)[3])))
"""


toggle((0, 0), (9, 2))
for row in all_lights:
    print row
counter = 0
for row in all_lights:
    for col in row:
        if col == 1:
            counter += 1
print counter
