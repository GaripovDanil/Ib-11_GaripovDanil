<<<<<<< HEAD
text = ''
i = 0
cat = 0
f_cat = -1

while text != 'СТОП':
    text = input()
    i += 1
    if 'Кот' in text or 'кот' in text:
        cat += 1
        if f_cat > -1:
            continue
        f_cat = i

print(cat, f_cat)
=======
text = ''
i = 0
cat = 0
f_cat = -1

while text != 'СТОП':
    text = input()
    i += 1
    if 'Кот' in text or 'кот' in text:
        cat += 1
        if f_cat > -1:
            continue
        f_cat = i

print(cat, f_cat)
>>>>>>> 83248a34b91166ffb865e00613c0f01f9d4f3b5b
