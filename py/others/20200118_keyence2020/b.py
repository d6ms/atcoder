N = int(input())
XL = [tuple(map(int, input().split())) for _ in range(N)]
XL.sort(key=lambda x: x[0] + x[1])

ans = 0
current = float('-inf')
for x, l in XL:
    if current <= x - l:
        current = x + l
        ans += 1
print(ans)

