import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
adj = [list() for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)


# 白 c == 0, 黒 c == 1
memo = dict()
def dfs(v, p, c):
    if memo.get((v, p, c)) is not None:
        return memo[(v, p, c)]
    if len(adj[v]) == 1 and adj[v][0] == p:
        ans = 1 if c == 1 else 2
        memo[(v, p, c)] = ans
        return ans
    ans = 0
    for color in [0, 1] if c == 0 else [0]:
        cans = 1
        for nxt in adj[v]:
            if nxt == p:
                continue
            cans = cans * dfs(nxt, v, color) % MOD
        ans = (ans + cans) % MOD
    memo[(v, p, c)] = ans
    return ans


root = None
for i, l in enumerate(adj):
    if len(l) > 1:
        root = i
        break

ans = dfs(root, -1, 0)
print(ans)
