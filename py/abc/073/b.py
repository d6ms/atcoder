N = int(input())
ans = 0
for l, r in [tuple(map(int, input().split())) for _ in range(N)]:
    ans += r - l + 1
print(ans)
