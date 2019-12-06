A, B, K = map(int, input().split())

for i in range(K):
    if i % 2 == 0:
        A = A if A % 2 == 0 else A - 1
        A //= 2
        B += A
    else:
        B = B if B % 2 == 0 else B - 1
        B //= 2
        A += B
print(A, B)
