import sys
from math import gcd

# 이미 심어져 있는 가로수 수 
N = int(sys.stdin.readline())

# 첫 가로수 위치 
a = int(sys.stdin.readline())

# 가로수들 사이의 값을 저장할 배열
arr = []

# 가로수들 사이의 간격 저장 
for i in range(N-1):
    num = int(sys.stdin.readline())
    arr.append(num - a)
    a = num

print(arr)
# arr에 들어있는 모든 수들의 최대공약수 찾기
g = arr[0]
for j in range(1, len(arr)):
    g = gcd(g, arr[j])
    print(g)
# 둘 사이에 심을 가로수 개수: 간격 // 최대공약수 - 1
result = 0
for each in arr:
    result += each // g - 1
print(result)