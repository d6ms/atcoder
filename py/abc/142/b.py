N, K = map(int, input().split())
h = list(map(int, input().split()))

ans = len(list(filter(lambda x: x >= K, h)))
print(ans)