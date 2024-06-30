# def solution(num_list):
#     answer = []
#     if num_list[-1] > num_list[-2]:
#         num_list.append(num_list[-1]-1)
#     else:
#         num_list.append(num_list[-1]*2)

#     return num_list

def solution(numlist):
    if (numlist[-1] > numlist[-2]):
        numlist.append((numlist[-1] - numlist[-2]))
    elif (numlist[-1] <= numlist[-2]):
        numlist.append(numlist[-1] * 2)
    return numlist