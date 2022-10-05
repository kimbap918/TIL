N = int(input()) # 수의 개수
arr = list(map(int, input().split())) # 수열 입력받기
plus, minus, mul, div = map(int, input().split()) # 연산자 개수 계산
# 최소, 최대값 초기화
max_val = -1e9
min_val = 1e9

def dfs(i, ary):
    global plus, minus, mul, div, max_val, min_val
    if i == N: # 수열을 수의 개수만큼 다 받았을경우 
        max_val = max(max_val, ary)
        min_val = min(min_val, ary)
    else:
        # 덧셈
        if plus > 0:
            plus -= 1
            dfs(i+1, ary + arr[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, ary - arr[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, ary * arr[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(ary / arr[i]))
            div += 1
dfs(1, arr[0])
print(max_val)
print(min_val)