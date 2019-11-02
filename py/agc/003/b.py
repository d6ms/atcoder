N = int(input())
lst = list()
cnt = 0
for _ in range(N):
    a = int(input())
    if a == 0:
        lst.append(cnt)
        cnt = a
    else:
        cnt += a
lst.append(cnt)

ans = 0
for cnt in lst:
    ans += cnt // 2
print(ans)
