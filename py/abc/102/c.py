N = int(input())
A = list(map(int, input().split()))

lst = list()
for i, a in enumerate(A):
    lst.append(a - i - 1)

lst.sort()
b = lst[N // 2]

ans = sum([abs(e - b) for e in lst])
print(ans)
