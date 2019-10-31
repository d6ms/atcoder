N = int(input())
S = input()

d = [0 for _ in range(N)]
d[0] = 1 if S[0] == '(' else -1
for i in range(1, N):
    if S[i] == '(':
        d[i] = d[i - 1] + 1
    else:
        d[i] = d[i - 1] - 1

if d[-1] < 0:
    d = [i for i in range(1, abs(d[-1]) + 1)] + [x - d[-1] for x in d]
m = min(d)
if m < 0:
    d = [i for i in range(1, abs(m) + 1)] + [x - m for x in d]
if d[-1] > 0:
    d = d + [i for i in reversed(range(d[-1]))]

ans = ''
for i, num in enumerate(d):
    if i == 0:
        ans += '('
    elif d[i] > d[i - 1]:
        ans += '('
    else:
        ans += ')'
print(ans)