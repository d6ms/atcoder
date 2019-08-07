X = int(input())

ans = 0
for i in range(1001):
    for e in range(2, 10):
        if i ** e > X:
            continue
        ans = max(ans, i ** e)
print(ans)
