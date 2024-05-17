import sys
import math
input = sys.stdin.readline 


# 주어진 자연수의 소인수 중 최댓감이 K보다 크지 않을 때
N = int(input()) # N보다 작거나 같은 자연수 중                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
K = int(input())
arr = [True for i in range(N+1)]

for i in range(2, int(math.sqrt(N)+1)):
    if arr[i] == True:
        j = 2 
        while i*j <= N:
            arr[i*j] = False
            j+=1
            
k_num = [1]*(N+1)
for i in range(2, N+1):
    if arr[i] and i > K:
        for j in range(i, N+1, i):
            k_num[j] = 0

print(sum(k_num)-1)

# 10 , 3
# 10 5 2 1



