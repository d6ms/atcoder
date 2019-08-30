def solve(S):
    max_count = 0
    count = 0
    for i in range(len(S)):
        if S[i] in ["A", "G", "C", "T"]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count


S = input()
print(solve(S))