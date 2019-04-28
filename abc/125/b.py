def solve(N, V, C):
    val = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            val += V[i] - C[i]
    return val

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))


print(solve(N, V, C))