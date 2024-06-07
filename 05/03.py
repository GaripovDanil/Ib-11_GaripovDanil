text = ''
i = 0
st = 0
yn = None

while text != 'СТОП':
    text = input()
    i += 1
    if 'Кот' in text or 'кот' in text:
        st = i
        yn = True

if yn:
    print(st)
else:
    print(-1)
