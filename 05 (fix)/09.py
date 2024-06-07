YN = None

for i in range(int(input())):
    text = input()
    if 'Кот' in text or 'кот' in text:
        YN = True
    if 'Пёс' in text or 'пёс' in text:
        YN = False

if YN:
    print("МЯУ")
else:
    print("НЕТ")
