a = input("Введите логин: ")
b = input("Введите адресс электронной почты: ")
if not'@' in a:
    if '@' in b:
        print("OK")
    else:
        print("error")
else:
    print("error")
