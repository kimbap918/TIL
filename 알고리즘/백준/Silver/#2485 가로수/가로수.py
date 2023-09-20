import sys

def GCD(A, B):
    while B != 0:
        tmp = A % B
        A = B
        B = tmp
    return A

# 가로수의 간격
N = int(sys.stdin.readline())
# 첫번째 가로수
a = int(sys.stdin.readline())
# 가로수 사이의 값 저장
arr = []

# 첫번째 입력을 제외하고 끝까지 돌면서
for i in range(N-1):
    n = int(sys.stdin.readline())
    # 2번째 입력부터 이전 입력값을 뺀것을 저장
    arr.append(n - a)
    a = n

# arr에 들어있는 모든 수들의 최대공약수 찾기
g = arr[0]
for j in range(1, len(arr)):
    g = GCD(g, arr[j])

# 두 가로수 사이에 심을 가로수의 개수는 간격 // 최대공약수 -1 
res = 0
for k in arr:
    res += k // g-1

print(res)