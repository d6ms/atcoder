N = int(input())
W1 = input()
past = set()
past.add(W1)
last = W1[-1]
ans = 'Yes'
for _ in range(N - 1):
    W = input()
    if W in past or not W.startswith(last):
        ans = 'No'
    else:
        past.add(W)
        last = W[-1]
print(ans)