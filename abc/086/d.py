N, K = map(int, input().split())
H = list()
for _ in range(N):
    x, y, c = input().split()
    x = int(x) % (2 * K)
    y = int(y) % (2 * K)
    H.append((x, y, c))

