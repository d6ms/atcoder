S = input()
for op1 in [1, -1]:
    for op2 in [1, -1]:
        for op3 in [1, -1]:
            num = int(S[0]) + op1 * int(S[1]) + op2 * int(S[2]) + op3 * int(S[3])
            if num == 7:
                ans = S[0]
                ans += '+' if op1 == 1 else '-'
                ans += S[1]
                ans += '+' if op2 == 1 else '-'
                ans += S[2]
                ans += '+' if op3 == 1 else '-'
                ans += S[3]
                ans += '=7'
                print(ans)
                exit(0)