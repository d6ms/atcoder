N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = A[0] * 4
ans += sum(A[1:M // 3]) * 6
if M % 3 == 0:
    ans += A[M // 3] * 2
elif M % 3 == 1:
    ans += A[M // 3] * 4
else:
    ans += A[M // 3] * 5
    ans += A[M // 3 + 1]

print(ans)