L, R = map(int, input().split())

if L // 2019 < R // 2019:
    print(0)
else:
    L %= 2019
    R %= 2019
    ans = float('inf')
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            m = i * j % 2019
            ans = min(ans, m)
    print(ans)