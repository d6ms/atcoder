def solve(H, A_B):
    max_a = 0
    for a_b in A_B:
        if a_b[0] > max_a:
            max_a = a_b[0]

    A_B.sort(key=lambda o: o[1], reverse=True)
    total_dmg = 0
    nage_count = 0
    for a_b in filter(lambda o: o[1] > max_a, A_B):
        total_dmg += a_b[1]
        nage_count+= 1
        if total_dmg >= H:
            return nage_count
    huri_count = int((H - total_dmg) / max_a)
    if H - total_dmg - (huri_count * max_a) <= 0:
        return nage_count + huri_count
    else:
        return nage_count + huri_count + 1


N, H = map(int, input().split())
A_B = [list(map(int, input().split())) for _ in range(N)]
print(solve(H, A_B))