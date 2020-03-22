import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

S = input()

def kaibun(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-i - 1]:
            return False
    return True

N = len(S)
l = S[:(N - 1) // 2]
r = S[(N + 3) // 2 - 1:]
print('Yes' if kaibun(S) and kaibun(l) and kaibun(r) else 'No')