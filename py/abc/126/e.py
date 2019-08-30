N, M = map(int, input().split())
nl = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    nl[X].append(Y)
    nl[Y].append(X)

seen = set()
ans = 0
stack = list()
for i in range(1, N + 1):
    if i not in seen:
        ans += 1
        stack.append(i)
        while len(stack) > 0:
            v = stack.pop()
            for next_v in nl[v]:
                seen.add(v)
                if next_v not in seen:
                    stack.append(next_v)
print(ans)
