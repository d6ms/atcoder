S = input()
T = int(input())

x = 0
y = 0
uk = 0
for c in S:
    if c == 'U':
        y += 1
    elif c == 'D':
        y -= 1
    elif c == 'R':
        x += 1
    elif c == 'L':
        x -= 1
    else:
        uk += 1

x = abs(x)
y = abs(y)
if T == 1:
    print(x + y + uk)
else:
    if x + y - uk < 0:
        uk = - (x + y - uk)
        if uk % 2 == 0:
            print(0)
        else:
            print(1)
    else:
        print(x + y - uk)