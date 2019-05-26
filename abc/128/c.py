N, M = map(int, input().split())
S = [list(map(int, input().split()))[1:] for _ in range(M)]
P = list(map(int, input().split()))

count = 0
for i in range(2 ** N):
    state = ''.join(list(reversed(str(bin(i))[2:].zfill(N))))
    flg = True
    for m in range(M):
        on = 0
        for s in S[m]:
            if state[s - 1] == '1':
                on += 1
        if on % 2 != P[m]:
            flg = False
            break
    if flg:
        count += 1
print(count)
