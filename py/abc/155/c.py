from collections import defaultdict

def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


N = I()
d = defaultdict(int)
for i in range(N):
    s = input()
    d[s] += 1

m = max(d.values())
ans = list()
for s, cnt in d.items():
    if cnt == m:
        ans.append(s)
ans.sort()
for x in ans:
    print(x)
