m = int(input())
n = int(input())
surname_m = set()
surname_n = set()

for i in range(m):
    surname = input()
    surname_m.add(surname)
for i in range(n):
    surname = input()
    surname_n.add(surname)

difference = len((surname_n - surname_m)) + len((surname_m - surname_n))
if not difference:
    print('NO')
else:
    print(difference)
