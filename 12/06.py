s = input()
print(*['-'.join(map(str.upper,i)) for i in s.split()])
