# トポロジカルソート
# 引数はすべて0-indexed、paddingなしの前提
# deg[i] := 頂点iの入次数
# returns := トポロジカルソートされた頂点番号のリスト
def tsort(deg, nl):
    tsorted = list()
    stack = [i for i, x in enumerate(deg) if x == 0]
    while len(stack) > 0:
        v = stack.pop()
        tsorted.append(v)
        for next_v in nl[v]:
            deg[next_v] -= 1
            if deg[next_v] == 0:
                stack.append(next_v)
    return tsorted
