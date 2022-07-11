# # 1 ~ 10000까지의 수
# # 양의 정수 n
# n = set(range(1, 10001))
# not_self_n = set() # set = 중복허용 안됨.

# for i in range(1, 10001): # 10000번동안
#     for j in str(i): # i를 문자형으로 변환
#         i += int(j) # 쪼갠 i를 j에 담아 i에 더하기 99(i) + 9(int(j) + 9(int(j))
#     not_self_n.add(i) # 셀프넘버가 아닌곳에 더한 i값 저장
# self_num = n - not_self_n
# for k in sorted(self_num):
#     print(k)

# 셀프넘버 = 전체숫자(1~10000) - 생성자(다른 숫자를 생성할 수 있는 수)
number = set(range(1, 10001)) # 1~10000 정수
not_self_number = set() # 셀프 넘버가 아닌 값을 받을 공간 

for i in range(1, 10001): # 10000번 동안
    for j in str(i): # i를 str로 변환
        i += int(j)  # 쪼갠 i를 j에 담아 i에 더하기 99(i) + 9(int(j)) + 9(int(j))
    not_self_number.add(i) # 셀프 넘버가 아닌 공간에 i값을 넣기
self_number = number - not_self_number # 셀프 넘버 = 전체 숫자 - 셀프넘버가 아닌 것

for k in sorted(self_number): # set은 정렬이 되어있지 않아 정렬한 값을 k에 넣어줌 
    print(k) # 출력
