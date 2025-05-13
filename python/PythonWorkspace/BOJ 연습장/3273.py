N = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0 
start, end = 0, N-1

# arr[0] = 1 
while start < end:
    interval_sum = arr[start] + arr[end]
    if interval_sum == x:
        cnt += 1
        start += 1
        end -= 1
    elif interval_sum < x:
        start += 1
    else:
        end -= 1
        
print(cnt)

# ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수

# N : 9 
# arr : 5 12 7 10 9 1 2 3 11
# x : 13

# ai + aj = 13 을 만족하는 쌍의 개수
# (10, 3), (11, 2), (12, 1)


# 1, 2, 3, 5, 7, 9, 10, 11, 12
# 