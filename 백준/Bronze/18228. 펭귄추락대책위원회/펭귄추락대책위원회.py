n = int(input())
data = list(map(int, input().split()))

index = 0
for i in range(len(data)) :
  if data[i] == -1 :
    index = i
    break

print(min(data[:index:]) + min(data[index+1::]))