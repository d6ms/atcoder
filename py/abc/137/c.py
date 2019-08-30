from collections import defaultdict

N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    s = [c for c in input()]
    s.sort()
    a = ''.join(s)
    cnt[a] += 1

ans = 0
for c, f in cnt.items():
    ans += f * (f - 1) // 2
print(ans)
