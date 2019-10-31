E = ''.join(sorted(list(input().split())))
B = input()
L = ''.join(sorted(list(input().split())))

matches = 0
for i in range(6):
    if L[i] in E:
        matches += 1

if matches < 3:
    print(0)
elif matches == 6:
    print(1)
elif matches == 5:
    for i in range(6):
        if L[i] not in E and L[i] == B:
            print(2)
            exit(0)
    print(3)
else:
    print(8 - matches)
