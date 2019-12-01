X = int(input())
for i in range(1001):
    if i * 100 <= X <= i * 100 + i * 5:
        print(1)
        exit(0)
print(0)
