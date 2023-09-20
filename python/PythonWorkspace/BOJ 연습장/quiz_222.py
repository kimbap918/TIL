mon, di = map(int, input().split())

if mon-(mon*(float("0."+str(di)))) >= 100:
  print("0")
else:
  print("1")