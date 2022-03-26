import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W = MI()
S = [list(input()) for _ in range(H)]


def next(i, j):
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if 0 <= i + di <= H - 1 and 0 <= j + dj <= W - 1:
            if S[i][j] != S[i + di][j + dj]:
                yield i + di, j + dj


ans = 0
seen = set()
for i in range(H):
    for j in range(W):
        p = i * W + j
        if p in seen:
            continue
        stack = [(i, j)]
        lseen = {i * W + j}
        while len(stack) > 0:
            h, w = stack.pop()
            lseen.add(h * W + w)
            seen.add(h * W + w)
            for next_h, next_w in next(h, w):
                if next_h * W + next_w not in seen:
                    stack.append((next_h, next_w))
        if len(lseen) >= 2:
            ans += len(lseen) * (len(lseen) - 1) // 2
        seen.update(lseen)
print(ans)