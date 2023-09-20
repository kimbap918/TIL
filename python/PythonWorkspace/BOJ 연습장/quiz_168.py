N = int(input())
# 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력한다. 
arr_len = list(map(int, input().split())) # 도시간의 거리
arr_oil = list(map(int, input().split())) # 도시의 주유 가격


ans = arr_len[0] * arr_oil[0] # 제일 왼쪽 도시에서 주유 (10)
min = arr_oil[0] # 제일 왼쪽 도시의 주유비 (5)
dist = 0 
for i in range(1, N-1):
    if arr_oil[i] < min: # 현재 주유 가격이 최소값보다 작으면 (2 < 5)
        ans += min*dist # 거리 * 주유가격을 곱해서 더해주고 (10 + 5*0) 
        dist = arr_len[i] # 거리를 갱신 (3)
        min = arr_oil[i] # 주유가격을 제일 작은 가격으로 갱신 (2)
    else:
        dist += arr_len[i]
    
    if i == N-2: # i가 arr_len의 값을 다 돌면
        ans += min*dist
print(ans)



