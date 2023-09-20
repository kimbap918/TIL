import sys
input = sys.stdin.readline
# 항상 가장 최상단에 존재하는 값이 의미가 없다면 pop을 해주는 것

# 왼쪽과 오른쪽
def solution(l, r):
    global heights
    if(l == r): 
        return heights[l]
    # 중간 = 오른쪽+왼쪽을 반으로 쪼갠 몫
    mid = (r + l) // 2
    # 반반 쪼개서 왼쪽과 오른쪽 중 큰것을 가져온다.
    area = max(solution(l, mid), solution(mid + 1, r))
    lmid  = mid
    rmid = mid + 1
    height = min(heights[lmid], heights[rmid])

    # 이전 구한 값과 중간 위치의 넓이를 비교해서 가장 큰 것은 가져 온다.
    area = max(area, height * 2, heights[lmid], heights[rmid])
    while (l < lmid or rmid < r):
        if(rmid < r and ((lmid <= l) or (heights[lmid - 1] < heights[rmid + 1]))):
            rmid += 1
            height = min(height, heights[rmid])
        else:
            lmid -= 1
            height = min(height, heights[lmid])
        area = max(area, height * (rmid - lmid + 1))
    return area

while 1:
    N, *heights = map(int, input().split())
    if  N == 0: break
    print(solution(0, N - 1))