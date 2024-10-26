t = int(input())
games=[]
for _ in range(t):
  games.append(input())
 
for game in games:
    if len(game) %2 == 0: 
      print(game[0::2])  
      print(game[1::2]) 
    else:
      print(game[0::2],game[1::2], sep='') 
      print(game[1::2],game[0::2],sep='')