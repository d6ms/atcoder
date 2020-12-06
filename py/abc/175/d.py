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

# マス i を含むループ1週の (スコア, ループ長)
score = [None] * N
for i in range(N):
    if score[i] is not None:
        continue
    route = {i}
    s = 0
    cur = i
    while True:
        next = P[cur] - 1
        s += C[next]
        if next in route:
            for j in route:
                score[j] = (s, len(route))
            break
        else:
            route.add(next)
            cur = next

ans = -INF
for i in range(N):
    lans = 0
    s, loop = score[i]
    if s >= 0:
        lans += s * (K // loop)
        rem = K - (K // loop * loop)
        if K // loop > 0:
            m_lans = lans
        else:
            m_lans = -INF
    else:
        rem = min(K, N)
        m_lans = -INF

    cur = i
    for _ in range(rem):
        next = P[cur] - 1
        lans += C[next]
        cur = next
        if lans > m_lans:
            m_lans = lans

    if m_lans > ans:
        ans = m_lans
print(ans)