def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


N = I()
A = LMI()

d = dict()
for a in A:
    if d.get(a) is None:
        d[a] = 1
    else:
        print('NO')
        exit(0)
print('YES')