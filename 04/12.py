n = int(input())
ans = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        ans += num
    else:
        ans -= num

print(ans)
