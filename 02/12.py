text = input()
Len = len(text)
money = 40 * Len
rub = money // 100
cop = money % 100
print(f"{rub} р. {cop} коп.")
