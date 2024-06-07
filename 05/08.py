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
