def solution(num_list):
    answer = -1
    mul = 1
    summ = 0
    for num in num_list:
        mul *= num
        summ += num
    summ = summ**2
    if mul < summ:
        answer = 1
    else:
        answer = 0
    # print(3*4*5*2*1) 120
    # print((3+4+5+2+1)**2) 225
    # answer = 0
    return answer
    
