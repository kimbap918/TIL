# import sys
# input = sys.stdin.readline
# N = int(input()) # 5
# a = []
# for _ in range(N):
#     num = int(input()) # 1, 3, 2, 4, 5
#     a.append(num)
    
# count = [0] * (max(a)+1) # 배열의 최대값 +1 
# # [0, 0, 0, 0, 0, 0]

# for i in a:
#     count[i] += 1 # [1, 2, 3, 4, 5]

# for i in range(1, len(count)): #  1부터 count 길이(6)
#     count[i] += count[i-1] # 
# # count = [0, 1, 2, 3, 4, 5]

# result = [0] * (len(a)) # a와 길이가 같은 결과 리스트 만들기

# for num in a:
#     idx = count[num] # count[1], count[2], count[3] .. 
#     result[idx - 1] = num # result[1-1] = result[0].. result[1]..
#     count[num] -= 1 # count[1] = 0, count[2] = 1, count[3] = 2..

# for res in result:
#     print(res)



import sys
input = sys.stdin.readline
n = int(input())
num_list = [0] * 10001 # 1부터 10000까지 값, 인덱스는 0부터 세기때문에 계산하기 편하게 10001

for _ in range(n):
    num_list[int(input())] += 1 # 입력된 값의 인덱스에 +1

for i in range(10001):
    if num_list[i] != 0: # 0보다 큰 요소를 갖는 인덱스를 찾아서 출력
        for j in range(num_list[i]):
            print(i)