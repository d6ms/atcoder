from operator import xor

N = int(input())
A = list(map(int, input().split()))


def multiples(n, m):
    # m以下のnの倍数を返す
    lst = list()
    num = n
    while True:
        if num <= m:
            lst.append(num)
            num += n
        else:
            break
    return lst


ans = [0] * (N + 1)
for i in reversed(range(1, N + 1)):
    s = 0
    for m in multiples(i, N):
        s += ans[m]
    s %= 2
    ans[i] = xor(s, A[i - 1])

s = sum(ans)
print(s)
if s != 0:
    print(' '.join([str(i) for i in range(1, N + 1) if ans[i] > 0]))


