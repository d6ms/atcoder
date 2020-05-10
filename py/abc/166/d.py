import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')



X = I()
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            exit(0)
