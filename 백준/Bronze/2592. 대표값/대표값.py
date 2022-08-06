a = []
a_dict = {}
max = 0

for _ in range(10):
    N = int(input())
    a.append(N)
    
for i in a: 
    if i not in a_dict: # 입력값이 딕셔너리 안에 없으면 
        a_dict[i] = 1 # 카운트 1
    else:
        a_dict[i] += 1 # 카운트 1 증가

ave_result = int(sum(a) / 10)

print(ave_result)
print(sorted(list(zip(a_dict.values(), a_dict.keys())))[-1][1])

# zip은 순회 가능한 객체를 인자로 받고
# 각 객체가 담고있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자를 반환
# 여기서는 a_dict.values()와 a_dict.keys()를 엮어 
# 10, 1
# 20, 1
# 30, 3 식으로 키와 값을 엮었다.
# [(1, 10), (1, 20), (1, 50), (2, 40), (2, 60), (3, 30)]
# -1은 튜플의 맨 마지막 (3, 30), 1은 튜플 내의 1번째 요소(30)을 꺼내온것.