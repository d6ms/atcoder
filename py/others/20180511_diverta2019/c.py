N = int(input())
cnt = 0
BX = 0
BA = 0
XA = 0
for _ in range(N):
    S = input()
    for i in range(1, len(S)):
        if S[i - 1] == 'A' and S[i] == 'B':
            cnt += 1
    if S[0] == 'B' and S[-1] == 'A':
        BA += 1
    elif S[0] == 'B':
        BX += 1
    elif S[-1] == 'A':
        XA += 1

if BA > 0:
    cnt += BA - 1
    if BX > 0:
        cnt += 1
        BX -= 1
    if XA > 0:
        cnt += 1
        XA -= 1
cnt += min(XA, BX)
print(cnt)
