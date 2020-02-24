def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


N = I()
X = LMI()

p = sum(X) // N
ans1 = sum([(x - p) ** 2 for x in X])
ans2 = sum([(x - p - 1) ** 2 for x in X])
print(min(ans1, ans2))