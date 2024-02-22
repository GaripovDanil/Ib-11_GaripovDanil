while True:
    pas_1 = input()
    pas_2 = input()

    if len(pas_1) < 8:
        print("Короткий!")
        continue
    elif pas_1 != pas_2:
        print("Различаются!")
        continue
    elif '123' in pas_1:
        print("Простой!")
        continue
    else:
        print("ОК")
        break
