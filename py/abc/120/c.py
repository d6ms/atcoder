def solve(S):
    zeros = 0
    ones = 0
    for i in range(len(S)):
        if S[i] == "0":
            zeros += 1
        elif S[i] == "1":
            ones += 1
    return len(S) - abs(zeros - ones)


S = input()
print(solve(S))
