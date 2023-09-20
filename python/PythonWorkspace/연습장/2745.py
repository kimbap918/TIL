N, B = input().rstrip.split()
#print(int(N, int(B)))

N = N[::-1]
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = 0

for i in range(len(N)):
  res += table.index(N[i]) * (int(B) ** i)


# enumerate : 인덱스(index)와 원소를 동시에 접근하면서 루프를 돌린다.
# 입력 ABCDE 36 
# 0 E / 1 D / 2 C / 3 B / 4 A 
# for i, n in enumerate(N):
#     print(i, n)
#     res += table.index(n) * (int(B) ** i)
print(res)