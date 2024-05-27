# 리스트에서 짝수만 필터링 하는 함수

input_num = list(map(int, input().split()))
ans = filter(lambda x: x%2==0, input_num)
print(list(ans))