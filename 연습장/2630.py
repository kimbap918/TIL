# 분할 정복 : 재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄어가는 방식
# 주어진 문제를 작은 사례로 나누고(Divide) 각각의 작은 문제들을 해결하여 정복(Conquer)
import sys
N = int(sys.stdin.readline()) # 종이 한 변의 길이
# 정사각형 칸들의 색 상태
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
# 파란색, 흰색 결과값을 담을 리스트
res = []

def paper_cnt(x, y, N):
    color = paper[x][y] # 색깔이 초기 값
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]: # color의 값이 현재 위치의 값과 다르다면
                paper_cnt(x, y, N//2) # 제 1사분면 
                paper_cnt(x, y+N//2, N//2) # 제 2사분면
                paper_cnt(x+N//2, y, N//2) # 제 3사분면
                paper_cnt(x+N//2, y+N//2, N//2) # 제 4사분면
                return
    if color == 0:
        res.append(0)
    else:
        res.append(1)


paper_cnt(0,0,N) # 시작지점
print(res.count(-1))
print(res.count(0))
print(res.count(1))