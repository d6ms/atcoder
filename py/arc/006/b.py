N, L = map(int, input().split())
amida = [input() for _ in range(L + 1)]

j = amida[-1].find('o')
for i in reversed(range(L)):
    if j > 0 and amida[i][j - 1] == '-':
        j -= 2
    elif j < 2 * (N - 1) and amida[i][j + 1] == '-':
        j += 2
print(j // 2 + 1)
