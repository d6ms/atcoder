K = int(input())
a = int(K / 2)
b = int(K / 2) if K % 2 == 0 else int(K / 2) + 1
print(a * b)