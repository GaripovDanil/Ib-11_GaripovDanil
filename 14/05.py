def triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        print('Это треугольник')
    else:
        print('это не треугольник')


a = int(input())
b = int(input())
c = int(input())
triangle(a, b, c)
