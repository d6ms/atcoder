N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in reversed(range(N)):
    m1 = min(B[i], A[i + 1])
    ans += m1
    m0 = min(B[i] - m1, A[i])
    A[i] -= m0
    ans += m0
print(ans)