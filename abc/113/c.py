N, M = map(int, input().split())
lst = list()
for i in range(M):
    P, Y = map(int, input().split())
    lst.append((Y, i, P))
lst.sort()

cnt = [1] * (N + 1)
ans = list()
for Y, i, P in lst:
    id = str(P).zfill(6) + str(cnt[P]).zfill(6)
    cnt[P] += 1
    ans.append((i, id))
ans.sort()
for i, id in ans:
    print(id)
