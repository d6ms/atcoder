N = int(input())

ans = 0
for _ in range(N):
    x, u = input().split()
    x = float(x)
    if u == 'JPY':
        ans += x
    elif u == 'BTC':
        ans += x * 380000
print(ans)