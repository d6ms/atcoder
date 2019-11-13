N = int(input())
A = [0] * (N + 2)
for i, a in enumerate(map(int, input().split())):
    A[i + 1] = a
costs = [0] * (N + 2)
for i in range(1, N + 2):
    costs[i] = abs(A[i] - A[i - 1])
cost = sum(costs)

for i in range(1, N + 1):
    actual = abs(A[i + 1] - A[i - 1])
    plan = abs(A[i] - A[i - 1]) + abs(A[i + 1] - A[i])
    print(cost - (plan - actual))

