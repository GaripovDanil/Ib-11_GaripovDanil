a = input()
if a <= '0.0000001' or a == '0':
    print(1000000)
else:
    print(1 / float(a))
