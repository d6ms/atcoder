def solve(b):
    if b == "A":
        return "T"
    if b == "T":
        return "A"
    if b == "G":
        return "C"
    if b == "C":
        return "G"


b = input()
print(solve(b))