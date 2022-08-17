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