N, M = map(int, input().split())
ac = [0] * N
wa = [0] * N

for p, S in [tuple(input().split()) for _ in range(M)]:
    p = int(p) - 1
    if S == 'WA' and ac[p] != 1:
        wa[p] += 1
        continue
    if S == 'AC':
        ac[p] = 1
pena = 0
for i in range(N):
    if ac[i] == 1:
        pena += wa[i]
print(sum(ac), pena)

