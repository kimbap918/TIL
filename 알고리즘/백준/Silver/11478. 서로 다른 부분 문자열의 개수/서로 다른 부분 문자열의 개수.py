S = input()
set_S = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j+1]
        set_S.add(temp)
print(len(set_S))