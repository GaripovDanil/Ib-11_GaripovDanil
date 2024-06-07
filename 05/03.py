<<<<<<< HEAD
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
=======
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
>>>>>>> 83248a34b91166ffb865e00613c0f01f9d4f3b5b
    print(-1)