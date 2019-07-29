S = input()

if len(S) == 1:
    print(0)

for i in range(11, 100):
    d0 = i % 10
    d1 = i // 10
    if (4 * d0 + d1) % 13 == 5:
        print(i)