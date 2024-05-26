step = int(input())
text = str(input())
for i in text:
    i = ord(i) + step
    print(chr(i), end='')
