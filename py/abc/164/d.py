import sys
sys.setrecursionlimit(300000)
from collections import Counter

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


S = input()

m = [0]
pow = 1
for i in range(len(S)):
    m.append((m[-1] + int(S[- i - 1]) * pow) % 2019)
    pow = (pow * 10) % 2019


ans = 0
for cnt in Counter(m).values():
    ans += cnt * (cnt - 1) // 2
print(ans)
