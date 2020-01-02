N, K = map(int, input().split())
R, S, P = map(int, input().split())
p = dict()
p['r'] = R
p['s'] = S
p['p'] = P
T = input()


def solve(me, you, memo):
    point = 0
    for i, t in enumerate(T):
        if t == you and (i < K or (i - K >= 0 and memo[i - K] != me)):
            memo[i] = me
            point += p[me]
    return point


m = ['' for _ in range(N)]
pri = [(R, 'r', 's'), (S, 's', 'p'), (P, 'p', 'r')]
pri.sort(reverse=True)
ans = 0
for _, i, u in pri:
    ans += solve(i, u, m)
print(ans)
