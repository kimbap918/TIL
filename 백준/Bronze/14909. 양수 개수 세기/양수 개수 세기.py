data = list(map(int, input().split()))
result = 0

for i in range(len(data)) :
  if data[i] > 0 :
    result += 1

print(result)