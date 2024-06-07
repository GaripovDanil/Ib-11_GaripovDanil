n = int(input())
YN = None

for i in range(n):
    text = input()
    if 'Кот' in text or 'кот' in text:
        YN = True

if YN:
    print("МЯУ")
else:
    print("НЕТ")
