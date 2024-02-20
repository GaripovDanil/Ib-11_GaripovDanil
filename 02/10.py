a = input()
b = input()
action = input()

if action == '/' and b == '0':
    print(888888)

if action == '+':
    print(float(a) + float(b))
elif action == '-':
    print(float(a) - float(b))
elif action == '*':
    print(float(a) * float(b))
elif action == '/':
    print(float(a) / float(b))
else:
    print(888888)
