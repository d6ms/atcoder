N = int(input())
S = input()

ans = 0
t = ''
for s in S:
    if s != t:
        ans += 1
        t = s
print(ans)
