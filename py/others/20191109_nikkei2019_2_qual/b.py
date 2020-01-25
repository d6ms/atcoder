from collections import defaultdict


# 累乗
def power(a, n, p):
    bi = str(format(n, "b"))  # 2進表現に
    res = 1
    for i in range(len(bi)):
        res = (res * res) % p
        if bi[i] == "1":
            res = (res * a) % p
    return res


N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

if D[0] != 0 or 0 in D[1:]:
    print(0)
    exit(0)

cnt = defaultdict(int)
for d in D:
    cnt[d] += 1

ans = 1
for i in range(1, max(D) + 1):
    if cnt.get(i) is None:
        print(0)
        exit(0)
    num = pow(cnt[i - 1], cnt[i], MOD)
    ans = ans * num % MOD
print(ans)
