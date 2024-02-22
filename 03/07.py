maximum = 1000
minimum = 1
number = maximum // 2
action = None

print('500')

while True:
    action = input()
    if action == '<':
        maximum = number
        number = ((maximum - minimum) // 2) + minimum
        print(number)
    if action == '>':
        minimum = number
        number = ((maximum - minimum) // 2) + minimum
        print(number)
    if action == '=':
        break
