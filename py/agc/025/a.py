import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


def digsum(num):
    ans = 0
    while num > 0:
        p, q = divmod(num, 10)
        num = p
        ans += q
    return ans

N = I()
ans = INF
for i in range(1, N // 2 + 1):
    ans = min(ans, digsum(i) + digsum(N - i))
print(ans)
