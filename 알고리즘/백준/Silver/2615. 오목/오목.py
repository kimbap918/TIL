n = 19 # 오목판의 크기
# 오목판의 크기만큼 반복하면서 바둑돌 좌표 입력값을 리스트로 저장
arr = [list(map(int, input().split())) for _ in range(n)]
 
dx = [1, 1, 0, -1]  # 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dy = [0, 1, 1, 1]    
 
def omok(): 
    for x in range(n): # 19
        for y in range(n): # 19
            if arr[x][y]:
                # 4방위 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    # 좌표가 오목판의 범위를 벗어나는 경우
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    # nx가 0보다 크거나 같고 n보다 작을때, ny가 0보다 크거나 같고, n보다 작을때, arr[x][y] == arr[nx][ny]일때까지
                    while 0 <= nx < n and 0 <= ny < n and arr[x][y] == arr[nx][ny]:
                        cnt += 1
                        # 5줄이 되는 경우
                        if cnt == 5:
                            
                            if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and arr[nx][ny] == arr[nx + dx[i]][ny + dy[i]]:  # 육목 판정 1
                                # print(n)
                                # print(nx + dx[i])
                                # print(ny + dy[i])
                                # print(arr[nx + dx[i]][ny + dy[i]])
                                break
                            if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and arr[x][y] == arr[x - dx[i]][y - dy[i]]:  # 육목 판정 2
                                # print(n)
                                # print(x - dx[i])
                                # print(y - dy[i])
                                # print(arr[x - dx[i]][y - dy[i]])
                                break
                            return arr[x][y], x+1, y+1  # 육목이 아닌 오목이면 return
 
                        nx += dx[i] # nx에 좌표 방위의 숫자 누적
                        ny += dy[i] # ny에 좌표 방위의 숫자 누적
    return 0, -1, -1  # 승부가 나지 않을 때
 
color, x, y = omok()
if not color:
    print(color)
else:
    print(color)
    print(x, y)