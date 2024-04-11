n = int(input())
c = set()

for i in range(n):
    b = input()
    c.add(b)

a = input()
if a not in c:
    print('OK')
else:
    print('TRY ANOTHER')
