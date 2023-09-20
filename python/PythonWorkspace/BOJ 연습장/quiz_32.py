A = []
N = int(input())
B = list(input().split())
temp = 0
max = -10000000
min = 10000000

for i in range(len(B)):
    A.append(B[i])

for j in range(len(B)): # 최대값
    if max < int(B[j]):
        max = int(B[j])

for k in range(len(B)): # 최소값
    if min > int(B[k]):
        min = int(B[k])

print(min, max)
