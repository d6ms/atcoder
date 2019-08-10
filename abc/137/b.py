K, X = map(int, input().split())

ans = ' '.join([str(i) for i in range(X - K + 1, X + K)])
print(ans)
