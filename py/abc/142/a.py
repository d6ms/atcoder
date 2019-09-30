N = int(input())

even = N // 2 if N % 2 == 0 else int(N / 2) + 1
print(even / N)