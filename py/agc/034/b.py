s = input()
arr = list()

i = 0
buf = ''
while i < len(s):
    if s[i] == 'A':
        if buf:
            arr.append(buf)
            buf = ''
        arr.append('A')
        i += 1
    elif s[i: i + 2] == 'BC':
        if buf:
            arr.append(buf)
            buf = ''
        arr.append('BC')
        i += 2
    else:
        buf += s[i]
        i += 1
if buf:
    arr.append(buf)

cnt = 0
stack = 0
for e in reversed(arr):
    if e == 'BC':
        stack += 1
    elif e == 'A':
        cnt += stack
    else:
        stack = 0
print(cnt)