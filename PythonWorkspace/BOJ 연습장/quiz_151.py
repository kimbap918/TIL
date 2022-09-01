import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 좌표평면 위 두 점 사이의 거리 공식 활용
    # (x-a)^2 + (y-b)^2 = r^2
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2) 
    if dist == 0 and r1 == r2: # 두 원이 동심원(중심이 같은 원)일 때
        print(-1)
    elif abs(r1-r2) == dist or r1 + r2 == dist: # 원이 내접원으로 한 점에서 만날때
        print(1)
    elif abs(r1-r2) < dist < (r1 + r2): # 점이 두 점에서 만날때 
        print(2)
    else:
        print(0)