password_1 = input("Введите пароль: ")
password_2 = input("Подтвердите пароль: ")

if len(password_1) < 8:
    print("Короткий.")
elif password_1 != password_2:
    print("Зазличаются.")
else:
    print("ОК")
