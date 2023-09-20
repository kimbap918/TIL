N = int(input())
for _ in range(N):
    n = int(input())
    
    clothes = {}
    for _ in range(n):
        # name은 입력만 받고 사용하지 않음 
        name, type = input().split()
        if type in clothes: # 딕셔너리에 값이 있으면 
            clothes[type] += 1 # +1
        else:
            clothes[type] = 1 # 없으면 1
#     (headgear + 1) * (eyewear + 1)으로 문제 해결
# - (옷의 종류 + 1) * (...) * ...
    case = 1 # 경우의 수
    for key in clothes.keys(): 
        # +1이 있는 이유는 그 종류의 의류를 입지 않는 경우를 포함한 것
        case = case * (clothes[key] + 1) # clothes[key]에 대한 값 + 1
    
    print(case - 1) # -1은 아무것도 입지 않은 경우의 수를 뺀것