a = int(input())
while str(a)[0] != '1' and a < 1000000000:
    a *= int(str(a)[0])
print(a)
