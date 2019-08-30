n = int(input())
v = list(map(int, input().split()))

evens = v[::2]
odds = v[1::2]


def means(arr):
    d = dict()
    for e in arr:
        if d.get(e) is None:
            d[e] = 1
        else:
            d[e] += 1
    m = sorted(d.items(), key=lambda e: e[1], reverse=True)
    m1, m1_cnt = m[0]
    m2, m2_cnt = m[1] if len(m) > 1 else (None, None)
    return (m1, m1_cnt), (m2, m2_cnt)


(e_m1, e_m1_cnt), (e_m2, e_m2_cnt) = means(evens)
(o_m1, o_m1_cnt), (o_m2, o_m2_cnt) = means(odds)

if e_m1 != o_m1:
    print(n - e_m1_cnt - o_m1_cnt)
else:
    if o_m2 is None and e_m2 is None:
        print(n // 2)
    else:
        candidate1 = n - e_m1_cnt - o_m2_cnt if o_m2_cnt is not None else float('inf')
        candidate2 = n - e_m2_cnt - o_m1_cnt if e_m2_cnt is not None else float('inf')
        print(min(candidate1, candidate2))
