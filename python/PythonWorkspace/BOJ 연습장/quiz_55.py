n =int(input()) # ex) 8
line = 0 # 대각선으로 그었을때 라인 
t_sum = 0 # 라인 1부터 n까지의 블럭 개수의 합

while n > t_sum: # t_sum이 n보다 작은 동안
    line += 1    # line 수 1씩 증가 1, 2, 3, (4)...
    t_sum += line # t_sum + 라인수의 누적 1, 3, 6, (10)...
# 8 = 2/3
# n : 2 line :2 t_sum : 3
if line % 2 == 0:
    mo = n - (t_sum - line) # 8 - (10 - 4) = 2
    ja = (t_sum - n) + 1 # (10 - 8) + 1 = 3
    print(str(mo)+"/"+str(ja))
elif line % 2 == 1:# 4, 5, 6 line : 3 t_sum : 6
    mo = (t_sum - n) + 1 
    ja = n - (t_sum - line) 
    print(str(mo)+"/"+str(ja))








# if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
#     top = line - gap  #분자
#     under = gap + 1  #분모
# else :  # 사선 라인이 홀수번째 일 때
#     top = gap + 1  #분자
#     under = line - gap  #분모
# print(f'{top}/{under}')