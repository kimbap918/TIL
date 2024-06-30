def solution(num_list):
    hol = []
    jjak = []
    for num in num_list:
        if num % 2 == 1:
            hol.append(str(num))
        else:
            jjak.append(str(num))
    answer = int(''.join(hol)) + int(''.join(jjak))

    return answer


# 3 5 1 = 351
#  4 2 = 42