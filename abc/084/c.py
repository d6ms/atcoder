N = int(input())
csf = [tuple(map(int, input().split())) for _ in range(N - 1)]

for i in range(N):
    t = 0
    for C, S, F in csf[i:]:
        if t < S:
            t = S + C
        elif t == S or t % F == 0:
            t += C
        else:
            t += F - t % F + C
    print(t)
