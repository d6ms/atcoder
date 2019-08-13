from collections import defaultdict
from itertools import combinations


N = int(input())
d = defaultdict(int)
for _ in range(N):
    S = input()
    if S[0] in 'MARCH':
        d[S[0]] += 1

ans = 0
for a, b, c in combinations('MARCH', 3):
    ans += d[a] * d[b] * d[c]
print(ans)