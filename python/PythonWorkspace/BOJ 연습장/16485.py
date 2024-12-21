# 변 AB의 길이 c와 변 AC의 길이 b가 주어질 때, 
# (선분 BM의 길이)÷(선분 CM의 길이)의 값을 구하는 프로그램을 작성하시오.

# 각 BAC의 이등분선과 변 BC의 교점을 M


# c, b = map(int, input().split())
# ratio = c/b
# print(ratio)
# # 9 3

# 이등분선 9/2, 3/2 = 4.5, 1.5
# 


c, b = map(int, input().split())
print(max(c,b)/min(c,b))