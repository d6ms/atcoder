import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


T = input()

ans = list()
for i, c in enumerate(T):
    if c == '?':
        if len(ans) > 0 and ans[-1] == 'D' and i < len(T) - 1 and T[i + 1] in '?D':
            ans.append('P')
        else:
            ans.append('D')
    else:
        ans.append(c)
print(''.join(ans))
