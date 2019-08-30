# コンテスト中は無理やりなビット全探索[alias bit全探索]をしたが、正しく書き換えた

N, M = map(int, input().split())
S = [list(map(int, input().split()))[1:] for _ in range(M)]
P = list(map(int, input().split()))

count = 0
for i in range(2 ** N):
    flg = True
    for m in range(M):
        on = 0
        for s in S[m]:
            if (i >> s - 1) & 1:
                on += 1
        if on % 2 != P[m]:
            flg = False
            break
    if flg:
        count += 1
print(count)
