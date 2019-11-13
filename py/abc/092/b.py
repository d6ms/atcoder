N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]


def f(a, D):
    i = 0
    while i * a + 1 <= D:
        i += 1
    return i


consumed = 0
for a in A:
    consumed += f(a, D)
print(X + consumed)
