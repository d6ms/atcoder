S = input()
s1 = int(S[0:2])
s2 = int(S[2:4])


if s1 >= 1 and s1 <= 12 and s2 >= 1 and s2 <= 12:
    print("AMBIGUOUS")
elif s2 >= 1 and s2 <= 12 and s1 >= 1 and s1 <= 12:
    print("AMBIGUOUS")
elif s1 >= 0 and s1 <= 99 and s2 >= 1 and s2 <= 12:
    print("YYMM")
elif s2 >= 0 and s2 <= 99 and s1 >= 1 and s1 <= 12:
    print("MMYY")
else:
    print("NA")
