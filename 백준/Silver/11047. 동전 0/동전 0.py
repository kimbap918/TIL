N, K = map(int, input().split()) # 10 4200
coin_lst = []
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)): # 역순으로 
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    # 4200//50000 = 0, 4200//10000 = 0, 4200//5000 = 0
    # 4200//1000 = 4, 200//500 = 0, 200//100 = 2
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복
    # 4200, 4200, 4200, 200, 200, 0
print(count)