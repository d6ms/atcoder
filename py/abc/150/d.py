from fractions import gcd
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A = list(map(lambda x: int(x) // 2, input().split()))

    v = A[0]
    for i in range(1, N):
        a, b = v, A[i]
        v = a * b // gcd(a, b)
        if v > M:
            print(0)
            exit(0)
    print((M // v + 1) // 2)


if __name__ == '__main__':
    main()
