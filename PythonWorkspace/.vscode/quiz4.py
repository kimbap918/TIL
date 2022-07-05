from random import *

users = range(1, 21) # 1부터 20까지 숫자를 생성

comment = set(users) # set 
comment1 = list(comment) # list
shuffle(comment1) # 리스트로 된 댓글을 섞음, set은 셔플이 안됨.
chicken = sample(comment1, 1) # 셔플된 리스트에서 값 하나를 추출

comment = comment - set(chicken) # 추출된 값을 set에서 제외
comment1 = list(comment)
coffee = sample(comment1, 3)

print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : " + str(chicken))
print("커피 당첨자 : " + str(coffee))
print("-- 축하합니다 --")
