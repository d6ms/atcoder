S = input()
K = int(input())

if all([c == '1' for c in S]):
    print(1)
    exit(0)

first_not1 = None
for i in range(len(S)):
    if S[i] != '1':
        first_not1 = i
        break

if K - 1 < first_not1:
    print(1)
else:
    print(S[first_not1])
