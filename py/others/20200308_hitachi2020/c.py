import sys
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


N = I()
nl = [list() for _ in range(N)]
for _ in range(N - 1):
    a, b = MI()
    nl[a - 1].append(b - 1)
    nl[b - 1].append(a - 1)

def solve(arr, mod):
    ans = [0] * N
    q = deque()
    q.append((0, -1, 0))
    while len(q) > 0:
        v, p, d = q.popleft()
        m = arr[d % 6]
        if mod[m] + m > N: return
        ans[v] = mod[m] * 3 + m
        mod[m] += 1
        mod[(m + 6) % 6] += 1
        for next_v in nl[v]:
            if next_v != p:
                q.append((next_v, v, d + 1))
    print(ans)
    exit(0)


solve([0, 1, 2, 0, 2, 1], [1, 0, 0])
solve([1, 2, 0, 2, 1, 0], [0, 0, 1])
solve([2, 0, 2, 1, 0, 1], [0, 1, 0])
print(-1)