import sys

T = int(input())

for i in range(T):
    # 높이(H), 너비(W), 몇번째 손님(N)
    # 6, 12, 10
    H, W, N = map(int, sys.stdin.readline().split())
    ho = N//H+1  # 손님의 수에서 높이를 나눈 몫+1이 호수
    floor = N % H # 손님의 수에서 높이를 나눈 나머지가 층
    if N % H == 0: # 손님의 수에 층을 나눈 나머지가 0이 나오는경우 
        ho = N//H # 손님의 수에 층을 나눈 몫 
        floor = H  # 층
    print(floor*100+ho) 


