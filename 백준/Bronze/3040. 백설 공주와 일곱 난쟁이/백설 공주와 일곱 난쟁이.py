data = [0] * 9
for i in range(0,9): #순서대로 입력 받아 리스트에 저장
  data[i] = int(input())
sum = sum(data)

for j in range(8):
  for k in range(j+1, 9):
    if sum - (data[j] + data[k]) == 100: 
      fake1 = data[j]
      fake2 = data[k]
      break

data.remove(fake1)
data.remove(fake2)
data.sort()
for i in data:
  print(i)