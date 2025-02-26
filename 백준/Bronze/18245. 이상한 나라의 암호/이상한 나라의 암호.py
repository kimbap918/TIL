idx = 1
while 1 :
  s = input()
  if s == 'Was it a cat I saw?' :
    break
  print(s[::idx+1])
  idx += 1
