num = int(input())
points = [list(map(int, input().split())) for _ in range(num)]
d = dict()
for i in range(num):
    square = points[i][0] // 10, points[i][1] // 10
    if square not in d:
        d[square] = 0
    d[square] += 1
print(max(d.values()))
