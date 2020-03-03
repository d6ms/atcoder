import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


N, K = MI()
AB = [tuple(MI()) for _ in range(N)]
AB.sort()

cnt = 0
for a, b in AB:
    if K <= cnt + b:
        print(a)
        exit(0)
    cnt += b
