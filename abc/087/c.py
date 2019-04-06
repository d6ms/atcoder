def solve(N, A):
    max_candies = 0
    # どこで下に降りるかの考え方がNケースあるだけ
    for j in range(1, N + 1):
        candies = sum(A[0][:j]) + sum(A[1][j - 1:])
        if candies > max_candies:
            max_candies = candies
    return max_candies


N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

print(solve(N, A))