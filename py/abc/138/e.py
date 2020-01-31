s = input()
t = input()

# next[i][c] = k : i文字目以降で最初にcが現れるのはk文字目 である (i < |s|)
N = len(s)
next = [dict() for _ in range(N)]
last = dict()
for i, c in enumerate(s + s):
    last_c = last[c] if last.get(c) is not None else -1
    for j in range(last_c + 1, min(i + 1, N)):
        next[j][c] = i % N
    last[c] = i

i = -1
for c in t:
    cur = i % N
    cur1 = (i + 1) % N
    if next[cur1].get(c) is None:
        print(-1)
        exit(0)
    n = next[cur1][c]
    if cur < n:
        i += n - cur
    elif n < cur:
        i += N - (cur - n)
    else:
        i += N
print(i + 1)
