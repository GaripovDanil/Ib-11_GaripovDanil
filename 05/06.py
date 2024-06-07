number = int(input())
i = 0
k = 0
while number != 0:
    if i < 10:
        i += number
        k += 1
    number = int(input())
print(k)
