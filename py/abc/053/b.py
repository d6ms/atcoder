s = input()

start = None
for i, a in enumerate(s):
    if a == 'A':
        start = i if start is None else start
    if a == 'Z':
        end = i
print(end - start + 1)