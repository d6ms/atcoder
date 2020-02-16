T = int(input())
for _ in range(T):
    n, g, b = map(int, input().split())
    hq = (n + 1) // 2
    lq = n - hq
    cycle, days = divmod(hq, g)
    ans = (g + b) * cycle - b
    if days > 0:
        ans += b
        ans += days
    if ans < n:
        print(n)
    else:
        print(ans)