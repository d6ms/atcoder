def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))

def to_cumsum(arr, pad=True):
    """
    1次元配列を累積和の1次元配列に変換する
    pad: 先頭に0の項を作る場合はTrue
    """
    cumsum = 0
    padding = 1 if pad else 0
    new = [0] * (len(arr) + padding)
    for i, e in enumerate(arr):
        cumsum += e
        new[i + padding] = cumsum
    return new


N = input()
# 上位桁で支払いきったときの各桁のおつり
ch = [None] * len(N)
for i, d in enumerate(N):
    ch[i] = 10 - int(d)
ch = to_cumsum(ch, pad=False)

ans = float('inf')
cnt = 0
for i, d in enumerate(N):
    d = int(d)
    # 1つ上の桁のお札で払い切る
    cur = cnt
    cur += d + 1 if d < 9 else 1  # 今の桁と後続が全て0の場合は？
    cur += ch[len(N) - 1] - ch[i]
    ans = min(ans, cur)
    # 今の桁のお札をピッタリ払う
    cnt += d
ans = min(ans, cnt)
print(ans)