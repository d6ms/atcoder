def solve(N, A):
    if len(list(filter(lambda x: x < 0, A))) % 2 == 0:
        return sum(map(abs, A))
    else:
        min_abs = min(map(abs, A))
        return sum(map(abs, A)) - 2 * min_abs


N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))