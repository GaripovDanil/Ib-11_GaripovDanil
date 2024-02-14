answer = input("Умеете ли вы читать?h \nВ ответ запишите да или нет: ")

if answer == "да" or answer == "Да":
    print("Прочитайте (Война и мир)")
elif answer == "нет" or answer == "Нет":
    print("Тогда как вы ответили на вопрос?")
else:
    print("Ошибка")
