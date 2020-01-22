N, K = map(int, input().split())
D = input().split()

while True:
    if any([c in D for c in str(N)]):
        N += 1
    else:
        print(N)
        break
