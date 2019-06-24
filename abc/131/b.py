N, L = map(int, input().split())

total_taste = 0
min_taste = float('inf')
for i in range(1, N + 1):
    taste = L + i - 1
    total_taste += taste
    if abs(taste) < abs(min_taste):
        min_taste = taste

print(total_taste - min_taste)
