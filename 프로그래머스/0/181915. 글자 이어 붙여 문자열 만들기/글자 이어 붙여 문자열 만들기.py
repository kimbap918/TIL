def solution(my_string, index_list):
    lis = []
    for i in index_list:
        lis.append(my_string[i])
    
    answer = ''.join(lis)
    return answer