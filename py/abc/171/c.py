import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N = I()
ans = ''
for i in range(1, 99):
    if N <= 26 ** i:
        N -= 1
        for j in range(i):
            ans += chr(ord('a') + N % 26)
            N //= 26
        break
    else:
        N -= 26 ** i
print(ans[::-1])
