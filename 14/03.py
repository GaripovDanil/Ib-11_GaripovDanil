def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print('I четверть')
    elif xcoord < 0 < ycoord:
        print('II четверть')
    elif xcoord < 0 and ycoord < 0:
        print('III четверть')
    elif xcoord > 0 > ycoord:
        print('IV четверть')
    else:
        print('Лежит на оси координат')


xcoord = int(input())
ycoord = int(input())
quarter(xcoord, ycoord)
