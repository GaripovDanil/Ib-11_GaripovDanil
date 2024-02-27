rang = int(input())
a = 1
b = 1

for a in range(1, rang + 1):
    a = a * b
    b = a
print(a)
