import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W, K = MI()
S = [None] * H
empty = set()
padding = [(0, 0)] * H
pad = 0
for i in range(H):
    S[i] = list(input())
    if all(c == '.' for c in S[i]):
        empty.add(i)
        pad += 1
    else:
        padding[i] = (pad, 0)
        pad = 0
if pad > 0:
    up, _ = padding[-pad - 1]
    padding[-pad - 1] = (up, pad)

color = 1
ans = [[0] * W for _ in range(H)]
for i in range(H):
    if i in empty:
        continue
    up, lp = padding[i]
    last = 0
    for j in range(W):
        if S[i][j] == '#':
            for x in range(last, j + 1):
                for y in range(-up, lp + 1):
                    ans[i + y][x] = color
            color += 1
            last = j + 1
    if S[i][-1] == '.':
        for x in range(last, W):
            for y in range(-up, lp + 1):
                ans[i + y][x] = color - 1

for l in ans:
    print(' '.join(str(c) for c in l))

