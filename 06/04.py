m = int(input())
n = int(input())
languages = set()
surnames = set()
for i in range(m + n):
    surname = input()
    if surname in languages:
        surnames.add(surname)
    else:
        languages.add(surname)
difference = languages - surnames
if not difference:
    print('NO')
else:
    print(len(difference))
