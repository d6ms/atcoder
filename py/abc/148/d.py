from math import isinf

N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
broke = 0
cur = 0
for i, a in enumerate(A):
    if a == cur + 1:
        cur += 1
        ans = min(ans, broke + N - i - 1)
    else:
        broke += 1
if isinf(ans):
    print(-1)
else:
    print(ans)
