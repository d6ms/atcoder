N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)] # N行M列

count = 0
for a in A:
    sum = 0
    for a_i, b_i in zip(a, B):
        sum += a_i * b_i
    sum += C
    if sum > 0:
        count += 1

print(count)
