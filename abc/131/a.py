S = input()

for i in range(3):
    if int(S[i + 1]) - int(S[i]) == 0:
        print('Bad')
        exit(0)
print('Good')
