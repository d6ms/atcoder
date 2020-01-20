from collections import defaultdict
import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7

def factorize(n):
    """
    nの値を素因数分解し、素因数とその指数をtupleにまとめたリストを返す
    e.g.
    [(2, 2), (5, 1)]
    """
    b = 2
    fct = []
    while b * b <= n:
        cnt = 0
        while n % b == 0:
            cnt += 1
            n //= b
        if cnt > 0:
            fct.append((b, cnt))
        b += 1
    if n > 1:
        fct.append((n, 1))
    return fct


def main():
    N = int(input())
    A = list(map(int, input().split()))

    d = defaultdict(int)
    for a in A:
        for num, f in factorize(a):
            d[num] = max(d[num], f)

    l = 1
    for num, f in d.items():
        l *= num ** f

    ans = 0
    for a in A:
        ans += l // a
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
