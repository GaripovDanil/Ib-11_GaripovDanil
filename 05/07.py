rang = int(input())
piece = 'Остазия'
war = 'Евразия'

for i in range(rang):
    command = input()

    if command == "С кем война?":
        print(war)

    if command == "С кем мир?":
        print(piece)

    if command == "Меняем":
        if piece == 'Остазия':
            piece = 'Евразия'
        else:
            piece = 'Остазия'

        if war == 'Остазия':
            war = 'Евразия'
        else:
            war = 'Остазия'
