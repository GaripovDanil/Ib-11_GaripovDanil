def game(text):
    if text.count(' ') % 2:
        print('Вы проиграли')
    else:
        print('Вы выиграли')


text = input()
game(text)
