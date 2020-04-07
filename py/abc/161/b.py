import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()
A = LMI()

s = sum(A)
print('Yes' if len(list(filter(lambda x: 4 * x * M >= s, A))) >= M else 'No')