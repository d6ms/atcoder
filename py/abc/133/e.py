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
            f.append(f[i - 1] * i)
    return f


MOD = 10 ** 9 + 7

N, K = map(int, input().split())
f = create_factorial(K)
nl = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    nl[a].append(b)
    nl[b].append(a)

ans = K
q = deque()
q.append((1, -1))  # 頂点番号、親頂点番号
while len(q) > 0:
    v, p = q.popleft()
    children = 0
    for next_v in nl[v]:
        if next_v != p:
            children += 1
            q.append((next_v, v))
    if children > 0:
        n = K - 1 if v == 1 else K - 2
        r = children
        perm = f[n] // f[n - r]
        ans = (ans * perm) % MOD

print(ans)