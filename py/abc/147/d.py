import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    A = list(map(int, input().split()))
    zeros = [0] * 60
    ones = [0] * 60
    for a in A:
        for i, c in enumerate(bin(a)[2:].zfill(60)):
            if c == '0':
                zeros[59 - i] += 1
            else:
                ones[59 - i] += 1
    ans = 0
    for i in range(60):
        ans += zeros[i] * ones[i] * (2 ** i)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
