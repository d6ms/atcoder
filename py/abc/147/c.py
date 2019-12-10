N = int(input())
shogens = [None] * N
for i in range(N):
    A = int(input())
    shogen = [None] * A
    for j in range(A):
        x, y = map(int, input().split())
        shogen[j] = (x, y)
    shogens[i] = shogen


def ok(i, shogens):
    for j in range(N):
        if (i >> j) & 1:
            for x, y in shogens[j]:
                if bin(i >> (x - 1))[-1] == str(y):
                    continue
                else:
                    return False
    return True


ans = 0
for i in range(2 ** N):
    if ok(i, shogens):
        ans = max(ans, bin(i).count('1'))
print(ans)
