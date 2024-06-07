text = ''
i = 0

while text != 'СТОП':
    text = input()
    i += 1
    if 'Кот' in text or 'кот' in text:
        print(i)
        break
else:
    print(-1)
