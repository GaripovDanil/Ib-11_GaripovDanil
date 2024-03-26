floor = int(input())
space = floor - 1

for i in range(1, floor + 1):
    print(space * ' ' + (i * 2 - 1) * '*')
    space -= 1
