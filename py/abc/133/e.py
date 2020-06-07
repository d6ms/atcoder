from collections import deque


def create_factorial(n):
    """
    階乗を事前計算した配列を作成します。
    :param n: [0, n]の配列を作成します
    """
    f = list()
    for i in range(n + 1):
        if i in [0, 1]:
            f.append(1)
        else:
            f.append(f[i - 1] * i % MOD)
    return f


MOD = 10 ** 9 + 7

N, K = map(int, input().split())
f = create_factorial(K)
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda s: int(s) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = K
q = deque()
q.append((0, -1))
while len(q) > 0:
    v, p = q.popleft()
    c = 0
    for nxt in adj[v]:
        if nxt != p:
            q.append((nxt, v))
            c += 1
    n = K - 1 if p == -1 else K - 2
    r = n - c
    if c > n:
        print(0)
        exit()
    ans = ans * (f[n] % MOD) * pow(f[r], MOD - 2, MOD) % MOD

print(ans)
