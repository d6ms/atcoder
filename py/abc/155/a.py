def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


A, B, C = MI()
if (A == B and B != C) or (A != B and B == C) or (A == C and B != C):
    print('Yes')
else:
    print('No')
