
A, B = map(int, input().split())
x = A
for i in range(A + 1, B + 1):
    x = x ^ i

print(x)