def number_to_words(n):
    f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    o = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто'}
    s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    n1 = n % 10
    n2 = n - n1
    if n < 10:
        return f.get(n)
    elif 10 < n < 20:
        return s.get(n)
    elif n >= 10 and n in o:
        return o.get(n)
    else:
        return o.get(n2) + ' ' + f.get(n1)


a = int(input())
print(number_to_words(a))
