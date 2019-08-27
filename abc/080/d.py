from heapq import heappop, heappush, heapify
from collections import defaultdict

N, C = map(int, input().split())

d = defaultdict(list)
for _ in range(N):
    s, t, c = tuple(map(int, input().split()))
    d[c].append((s, t))
stc = list()
for c, lst in d.items():
    if len(lst) == 1:
        s, t = lst[0]
        stc.append((s, t, c))
        continue
    lst.sort()
    s0, t0 = lst[0]
    i = 1
    while i < len(lst):
        s1, t1 = lst[i]
        if t0 == s1:
            t0 = t1
            if i == len(lst) - 1:
                stc.append((s0, t0, c))
        else:
            stc.append((s0, t0, c))
            s0 = s1
            t0 = t1
        i += 1

heapify(stc)
end = []
ans = 0
while len(stc) > 0:
    s, t, c = heappop(stc)
    if len(end) > 0:
        endtime = heappop(end)
        if endtime >= s:
            heappush(end, endtime)
    heappush(end, t)
    ans = max(ans, len(end))
print(ans)