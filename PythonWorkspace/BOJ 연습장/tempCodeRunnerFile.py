N = int(input())

for i in range(N):
  X, Y = map(int, input().split())
  
for x in range(X):
  rank = 1
  for y in range(Y):
    if X[0] < X[1] and Y[0] < Y[1]:
      rank += 1
print(rank, end= ' ')