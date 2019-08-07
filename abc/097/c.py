from itertools import combinations

s = input()
K = int(input())

cand = set()
for c in s:
    cand.add(c)
for l, r in combinations(range(len(s)), 2):
    if r - l + 1 > K:
        continue
    cand.add(s[l:r + 1])

cand = list(cand)
cand.sort()

print(cand[K - 1])