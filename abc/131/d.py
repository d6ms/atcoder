N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]
tasks.sort(key=lambda t: t[1])

timestamp = 0
for A, B in tasks:
    timestamp += A
    if B < timestamp:
        print('No')
        exit(0)
print('Yes')
