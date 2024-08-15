k = int(input())

for _ in range(k) :
  p, m = map(int, input().split())
  data = [0] * (m + 1)
  count = 0

  for _ in range(p) :
    value = int(input())
    if data[value] == 0 :
      data[value] = 1
    else :
      count += 1

  print(count)