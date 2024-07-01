def solution(n):
    cnt = 1
    board = [[0] * n for i in range(n)]
    top = 0
    bottom = n-1 # 3
    left = 0
    right = n-1 # 3
    
    # 위에서 아래로, 좌에서 우로
    while top <= bottom and left <= right:
        
        # [0, 0], [0, 1], [0, 2], [0, 3]
        for i in range(left, right+1): # 0~3
            board[top][i] = cnt # 0, 0 1 2 3
            cnt+=1
        top += 1
        # [1, 3]
            
        # [1, 3], [2, 3], [3, 3]
        for i in range(top, bottom+1): # 1~3
            board[i][right] = cnt
            cnt+=1
        right -= 1
        # [3, 2]
        
        # top 4, bottom 3, right 2, left 0
        if top <= bottom:
            # 우에서 좌로 이동
            for i in range(right, left - 1, -1):
                board[bottom][i] = cnt
                cnt += 1
            bottom -= 1
        
        if left <= right:
            # 아래에서 위로 이동
            for i in range(bottom, top - 1, -1):
                board[i][left] = cnt
                cnt += 1
            left += 1
        
    return board

#     [0][0]
#     [0][1]
#     [0][2]
#     [0][3]
#     [1][3]
#     [2][3]
#     [3][3]
#     [3][2]
#     [3][1]
#     [3][0]
#     [2][0]
#     [1][0]
#     [1][1]
#     [1][2]
#     [2][2]
#     [2][1]
    