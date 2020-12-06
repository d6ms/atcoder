import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, K = MI()
P = LMI()
C = LMI()

def loops():
    seen = set()
    for i in range(N):
        if i in seen:
            continue
        route = {i}
        s = 0
        cur = i
        while True:
            seen.add(cur)
            next = P[cur] - 1
            s += C[next]
            if next in route:
                yield s, route
                break
            else:
                route.add(next)
                cur = next

ans = -INF
for score, route in loops():
    if score > 0:
        lans = score * (K // len(route))
        times = K - (K // len(route) * len(route))
    else:
        lans = 0
        times = min(K, N)

    max_s = -INF
    route = list(route)
    for i in range(len(route)):
        s = 0
        cur = route[i]
        for _ in range(times):
            next = P[cur] - 1
            s += C[next]
            cur = next
            max_s = max(max_s, s)
    if score > 0:
        lans += max(0, max_s)
    else:
        lans += max_s
    ans = max(ans, lans)
print(ans)