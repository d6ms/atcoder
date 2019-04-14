inp = input().split()
A = int(inp[0])
B = int(inp[1])

result = 0
if A > B:
    result += A
    A -= 1
else:
    result += B
    B -= 1
if A > B:
    result += A
    A -= 1
else:
    result += B
    B -= 1

print(result)