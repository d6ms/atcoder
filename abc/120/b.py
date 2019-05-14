def solve(A, B, K):
    yakusu = list()
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            yakusu.append(i)
    return yakusu[-K]


A, B, K = map(int, input().split())
print(solve(A, B, K))
