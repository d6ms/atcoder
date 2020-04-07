import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N, K, C = MI()
S = input()

L = list()
i = 0
while i < N:
    if len(L) >= K:
        break
    elif S[i] == 'o':
        L.append(i)
        i += C + 1
    else:
        i += 1

R = list()
i = N - 1
while i >= 0:
    if len(R) >= K:
        break
    elif S[i] == 'o':
        R.append(i)
        i -= C + 1
    else:
        i -= 1
R.reverse()

for i in range(K):
    if L[i] == R[i]:
        print(L[i] + 1)
