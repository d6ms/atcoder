N = int(input())
P = list(map(int, input().split()))

Ps = sorted(P)

cnt = 0
for i in range(len(P)):
    if P[i] != Ps[i]:
        cnt += 1
if cnt in [0, 2]:
    print('YES')
else:
    print('NO')