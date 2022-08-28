import sys
input = sys.stdin.readline

# 3
# 6
# 34
# 38
N = int(input())
arr = []

for i in range(N):
    n = int(input())
    arr.append(n) # [6, 34, 28]

gcds = [abs(arr[1]-arr[0])] # 34 - 6 = 28

def gcd(a,b): # 4, 28
    if b == 0:
        return a
    # print(gcd(b, a%b))
    return gcd(b, a%b) # 28, 6 / 6, 4 / 4, 2 / 2, 0 => 2 return

for j in range(2, len(arr)):
    gcds.append(gcd(abs(arr[j] - arr[j - 1]), gcds[0])) # (arr[2] - arr[1])(28-34= 6), 28
gcds.sort() # 오름차순 정렬
ans = []
for k in range(1, int(gcds[0] ** 0.5) + 1): # gcds 첫번째 요소의 제곱근까지만 탐색
    if gcds[0] % k == 0: # 2 % 1 = 0
        ans.append(k) # 1
        ans.append(gcds[0] // k) # 2 // k = 2
ans = list(set(ans)) # 2
ans.sort()

for l in ans[1:]: # m이 1보다 커야하므로
    print(l, end=" ")
