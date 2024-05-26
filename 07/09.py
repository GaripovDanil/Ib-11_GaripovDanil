text = str(input())
a = int(input())
if a > len(text):
    print('ОШИБКА')
else:
    for j in range(len(text)):
        i = j + 1
        print(str(text[a - i]))
        break
