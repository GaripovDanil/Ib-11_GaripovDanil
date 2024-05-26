s1 = str(input())
while True:
    s2 = input()
    if s1[-1] == s2[0]:
        s1 = s2
    else:
        print(s2)
        break
