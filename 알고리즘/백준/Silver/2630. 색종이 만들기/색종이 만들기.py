import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

res = []

def paper_cnt(x, y, N) :
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :
        paper_cnt(x, y, N//2)
        paper_cnt(x, y+N//2, N//2)
        paper_cnt(x+N//2, y, N//2)
        paper_cnt(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    res.append(0)
  else :
    res.append(1)


paper_cnt(0,0,N)
print(res.count(0))
print(res.count(1))