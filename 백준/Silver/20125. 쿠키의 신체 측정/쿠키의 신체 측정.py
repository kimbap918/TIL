
N = int(input())
board = [input() for _ in range(N)]
res = []

def find_heart():        
    flag = False
    for i in range(N):
        for j in range(N):
            if board[i][j] != "_":
                head = [i, j]
                heart = [i+1, j]
                flag = True
                break
        if flag:
            break
    return head, heart

head, heart = find_heart()

def find_arms(heart): 
    i, j = heart[0], heart[1]-1
    cnt_L = 0
    cnt_R = 0
    while j > -1:
        if board[i][j] == "*":
            cnt_L += 1
            j-=1
        else:
            break

    i, j = heart[0], heart[1]+1

    while j < N:
        if board[i][j] == "*":
            cnt_R += 1
            j+=1
        else:
            break  

    return cnt_L, cnt_R

arm_l, arm_r = find_arms(heart)

def find_waist(heart):
    i, j = heart[0]+1, heart[1]
    cnt = 0

    while i < N:
        if board[i][j] == "*":
            cnt += 1
            i += 1
        else:
            leg = i, j
            break

    return cnt, leg

waist, leg = find_waist(heart)

def find_legs(leg):
    i, j = leg[0], leg[1]-1
    cnt_L = 0
    cnt_R = 0

    while i < N:
        if board[i][j] == "*":
            cnt_L += 1
            i += 1
        else:
            break

    i, j = leg[0], leg[1]+1

    while i < N:
        if board[i][j] == "*":
            cnt_R += 1
            i += 1
        else:
            break

    return cnt_L, cnt_R

leg_l, leg_r = find_legs(leg)

res.append([arm_l, arm_r, waist, leg_l, leg_r])

print(heart[0]+1, heart[1]+1)
print(' '.join(map(str, res[0])))

