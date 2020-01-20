from fractions import gcd
import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    A = list(map(int, input().split()))

    l = A[0]
    for i in range(1, N):
        l = l * A[i] // gcd(l, A[i])

    print(sum([l // a for a in A]) % MOD)


if __name__ == '__main__':
    main()
