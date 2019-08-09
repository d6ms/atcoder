N = int(input())
a = list(map(int, input().split()))

n = max(a)
a.remove(n)
d = list(map(lambda ai: abs(n / 2 - ai), a))
i = d.index(min(d))
r = a[i]

print(n, r)
