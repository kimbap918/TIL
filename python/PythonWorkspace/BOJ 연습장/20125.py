N = int(input())
board = [input() for _ in range(N)]

def find_heart():        
    for i in range(N):
        for j in range(N):
            if board[i][j] == "*":
                return [i, j], [i+1, j]

head, heart = find_heart()

def find_arms(heart): 
    i, j = heart[0], heart[1]
    cnt_L = cnt_R = 0
    
    for d in range(1, N):
        if j-d >= 0 and board[i][j-d] == "*":
            cnt_L += 1
        else:
            break
    
    for d in range(1, N):
        if j+d < N and board[i][j+d] == "*":
            cnt_R += 1
        else:
            break

    return cnt_L, cnt_R

def find_waist(heart):
    i, j = heart[0]+1, heart[1]
    cnt = 0
    while i < N and board[i][j] == "*":
        cnt += 1
        i += 1
    return cnt, [i, j]

def find_legs(leg):
    cnt_L = cnt_R = 0
    i = leg[0]
    for d in range(i, N):
        if board[d][leg[1]-1] == "*":
            cnt_L += 1
        else:
            break
    for d in range(i, N):
        if board[d][leg[1]+1] == "*":
            cnt_R += 1
        else:
            break
    return cnt_L, cnt_R

arm_l, arm_r = find_arms(heart)
waist, leg = find_waist(heart)
leg_l, leg_r = find_legs(leg)

print(heart[0]+1, heart[1]+1)
print(arm_l, arm_r, waist, leg_l, leg_r)
