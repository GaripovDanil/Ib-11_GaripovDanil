num = int(input())
dividers = 0
for i in range(1, num + 1):
    if num % i == 0:
        dividers += 1
        print(i, end=' ')

if dividers == 2:
    print("\nПРОСТОЕ")
else:
    print("\nНЕТ")
