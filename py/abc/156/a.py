def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


N, R = MI()
if N >= 10:
    print(R)
else:
    print(R + 100 * (10 - N))