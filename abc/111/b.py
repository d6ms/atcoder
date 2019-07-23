N = int(input())

for i in range(N, 1112):
    matched = True
    for j in range(1, len(str(i))):
        if str(i)[j - 1] != str(i)[j]:
            matched = False
            break
    if matched:
        print(i)
        exit(0)