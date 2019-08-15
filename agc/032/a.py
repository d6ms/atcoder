N = int(input())
B = list(map(int, input().split()))

ans = list()
for k in reversed(range(N)):
    hit = False
    for l in reversed(range(1, k + 2)):
        if B[l - 1] == l:
            B = B[:l - 1] + B[l:]
            hit = True
            ans.append(l)
            break
    if not hit:
        print(-1)
        exit(0)

for e in reversed(ans):
    print(e)
