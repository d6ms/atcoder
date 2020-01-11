from fractions import gcd
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A = list(map(lambda x: int(x) // 2, input().split()))

    X = A[0]
    for i in range(1, N):
        a, b = X, A[i]
        X = a * b // gcd(a, b)
        if X > M:
            print(0)
            exit(0)

    cnt = 0
    tmp = X
    while tmp % 2 == 0:
        tmp = tmp // 2
        cnt += 1
    for a in A:
        if a % (2 ** cnt) == 0 and a % (2 ** (cnt + 1)) != 0:
            continue
        else:
            print(0)
            exit(0)
    print((M // X + 1) // 2)


if __name__ == '__main__':
    main()
