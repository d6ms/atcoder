def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


N, M = MI()
C = [tuple(MI()) for _ in range(M)]

start = 0 if N == 1 else 10 ** (N - 1)
for i in range(start, 10 ** N):
    num = str(i)
    flg = True
    for s, c in C:
        if int(num[s - 1]) != c:
            flg = False
    if flg:
        print(num)
        exit(0)
print(-1)
