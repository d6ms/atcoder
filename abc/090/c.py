N, M = map(int, input().split())

# 周囲に偶数個のマスがあるものが裏返る
# 角と辺のマスを除けば良い
print(abs(N * M - (2 * N + 2 * M - 4)))