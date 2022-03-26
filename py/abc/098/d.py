def sum_equals_xor(num1, num2):
    for i in range(min(num1.bit_length(), num2.bit_length())):
        if (num1 >> i) & 1 and (num2 >> i) & 1:
            return False
    return True


N = int(input())
A = list(map(int, input().split()))

memo = [[-1 for _ in range(N)] for _ in range(N)]
ans = 0
for l in range(N):
    for r in range(l, N):
        if memo[l][r - 1] != -1 :
            s = memo[l][r - 1]
            if sum_equals_xor(s, A[r]):
                ans += 1
                memo[l][r] = s + A[r]
            else:
                break
        else:
            if l == r:
                ans += 1
                memo[l][r] = A[r]
            elif sum_equals_xor(A[l], A[r]):
                ans += 1
                memo[l][r] = A[l] + A[r]
print(ans)
