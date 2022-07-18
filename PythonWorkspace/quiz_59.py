# N = int(input()) # 설탕의 무게
# cnt = 0          # 봉지의 개수 
# while N >= 0: # 설탕이 0보다 크거나 같은동안
#     if N % 5 == 0: # 5의 배수이면
#         cnt += (N // 5) # 봉지개수는 N을 5로 나눈 몫
#         print(cnt)
#         break
#     N = N - 3 # N이 0이 될때까지 -3
#     cnt += 1  # 봉지 증가
# else:
#     print(-1)   



N = int(input())
cnt = 0
while N >= 0:
    if N % 5 == 0:
        cnt += (N//5)
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)