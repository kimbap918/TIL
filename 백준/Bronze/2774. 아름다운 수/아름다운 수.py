t = int(input())

for _ in range(t) :
  x = input()
  data = []

  result = 0
  for i in range(len(x)) :
    if int(x[i]) not in data :
      result += 1
      data.append(int(x[i]))

  print(result)