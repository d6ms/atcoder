N = int(input())
S_P_I = list()

for i in range(N):
    s, p = tuple(input().split())
    S_P_I.append((s, int(p), i + 1))

S_P_I = sorted(S_P_I, key=lambda spi: spi[1], reverse=True)
S_P_I = sorted(S_P_I, key=lambda spi: spi[0])

for s, p, i in S_P_I:
    print(i)