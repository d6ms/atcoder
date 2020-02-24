def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD=10 ** 9 + 7


C1 = input()
C2 = input()
if C1 == C2[-1] + C2[1] + C2[0] and C2 == C1[-1] + C1[1] + C1[0]:
    print('YES')
else:
    print('NO')
