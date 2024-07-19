def cal_score(x,y):
    score=0
    distance=x**2+y**2
    if distance<=9 :
        score = 100
    elif distance<=36 :
        score = 80
    elif distance<=81 :
        score = 60
    elif distance<=144 :
        score = 40
    elif distance<=225 :
        score = 20
    else :
        score = 0
    return score
def sol(nums):
    p1_score,p2_score=0,0
    for i in range(3):
        p1_score+=cal_score(nums[2*i],nums[2*i+1])
    for i in range(3,6):
        p2_score += cal_score(nums[2 * i], nums[2 * i + 1])
 
    if p1_score>p2_score:
        print('SCORE: %d to %d, PLAYER 1 WINS.'%(p1_score,p2_score))
    elif p1_score==p2_score:
        print('SCORE: %d to %d, TIE.'%(p1_score,p2_score))
    else:
        print('SCORE: %d to %d, PLAYER 2 WINS.'%(p1_score,p2_score))
 
 
for _ in range(int(input())):
    nums=list(map(float, input().split()))
    sol(nums)
