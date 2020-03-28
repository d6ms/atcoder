import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


S = input()
print('Yes' if S[2] == S[3] and S[4] == S[5] else 'No')