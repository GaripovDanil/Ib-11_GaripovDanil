b = 1
c = 1
for a in range(1, 7):
    c = int(input())
    if c == 0:
        continue
    b *= c
print(b)
