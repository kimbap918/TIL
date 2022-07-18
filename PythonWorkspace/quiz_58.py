# T = int(input())

# for i in range(T): # 케이스 수
#     k = int(input()) # 층 1
#     n = int(input()) # 호 3 = 1+2+3 = 6명
#     # 2층 3명? 1+2+3
#     # a층의 b호에 살려면 a-1층의 1호 부터 b호까지 사람들의 수 합만큼 
#     # 사람들을 데려와 살아야함
#     f0 = []
#     # f0 = [x for x in range(1, n)]
#     for x in range (1, n+1): # 기본이 되는 0층의 값을 삽입
#         f0.append(x)
#     for j in range(k): # 층의 수만큼 반복
#         for h in range(1, n): # 1 ~ n-1
#             f0[h] += f0[h-1] # f0[h]에 f0[h-1](h 이전의 값)을 합산
#     print(f0[-1]) # 역순으로 출력

T = int(input())

for i in range(T): # 테스트케이스의 수
  k = int(input()) # 층수를 나타냄
  n = int(input()) # 호수를 나타냄
  f0 = [] # 계산의 기본이 될 0층
  for j in range(1, n+1): # 1부터 n까지의 범위
    f0.append(j)
  for h in range(k): # 층의 수만큼 반복한다.
    for w in range(1, n):
        f0[w] += f0[w-1] # f0[w]의 값은 그 이전의 값의 누적
print(f0[-1])





     

