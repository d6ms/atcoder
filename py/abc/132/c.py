N = int(input())
D = list(map(int, input().split()))
D.sort()

ans = D[int(N / 2)] - D[int((N / 2) - 1)]
print(ans)