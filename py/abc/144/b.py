N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == N:
            print('Yes')
            exit(0)
print('No')