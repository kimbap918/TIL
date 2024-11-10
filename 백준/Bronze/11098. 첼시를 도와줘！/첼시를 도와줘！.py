n = int(input())

for _ in range(n) :
  p = int(input())
  max_price = 0
  max_name = ""
  for _ in range(p) :
    c, name = input().split()
    if int(c) > max_price :
      max_price = int(c)
      max_name = name
  
  print(max_name)