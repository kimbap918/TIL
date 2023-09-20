N, B = input().rstrip().split()
#print(int(N, int(B)))


N = N[::-1]
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = 0

for i in range(len(N)):
    res += table.index(N[i]) * (int(B) ** i)
print(res)