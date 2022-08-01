# 시작은 무조건 0(딸기우유)
n = int(input())
milk = list(map(int,input().split()))
# print(milk)

count = 0 # 딸기우유(0)

for i in range(n): # n의 횟수만큼
    if milk[i] == count % 3: # 리스트 값이 카운트 나누기 3의 나머지와 같으면
        count += 1 # 카운트 증가 

print(count)