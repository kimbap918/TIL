n_list = list(map(int,input().split()))
odd = []

for i in range(3):
    if (n_list[i] %2) != 0:
        odd.append(n_list[i])
ans = 1
if not odd:
    for i in range(3):
        ans *= n_list[i]

else:
    for i in range(len(odd)):
        ans *= odd[i]
print(ans)