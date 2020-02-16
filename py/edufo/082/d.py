from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i, a in enumerate(A):
        (n & (n - 1)) == 0 # 2べき判定
        n.bit_length()
        if a <= n:
            n -= a
        else:
            A = A[i:]
            break

