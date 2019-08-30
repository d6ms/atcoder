
def solve(N, Y):
    # すべて1000円札で賄えるか検証
    if N * 1000 >= Y:
        return 0, 0, Y / 1000
    # 全探索
    for gosen in range(0, N + 1):
        for man in range(0, N - gosen + 1):
            sen = N - gosen - man
            if man * 10000 + gosen * 5000 + sen * 1000 == Y:
                return man, gosen, sen
    return -1, -1, -1


N, Y = map(int, input().split())
man, gosen, sen = solve(N, Y)
print(int(man), int(gosen), int(sen))