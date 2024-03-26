sec = int(input())
a = sec

for i in range(sec):
    print("Осталось секунд: " + str(a))
    a -= 1
else:
    print("Пуск")
