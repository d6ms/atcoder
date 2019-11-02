from itertools import combinations


N, K = map(int, input().split())

# 最短距離が2であるような頂点のペアの数の最大値は (N-1)(N-2)/2 で、これはスター型のトポロジをつくった時
# 最小値は 0 で、これは完全グラフを構築した時
max_pairs = int((N - 1) * (N - 2) / 2)
if K > max_pairs:
    print(-1)
    exit(0)

# スター型のトポロジを作ると辺の数は N - 1 本
# 周辺の頂点に1ペアを作るごとに辺を1本足す必要がある
M = N - 1 + max_pairs - K
print(M)

# スターの中心には頂点Nを配置することにする
for i in range(1, N):
    print(i, N)
if K == max_pairs:
    exit(0)

# Kペアになるまで周辺の頂点をつないでいく
pairs = max_pairs
for a, b in combinations(range(1, N), 2):
    print(a, b)
    pairs -= 1
    if pairs == K:
        exit(0)
