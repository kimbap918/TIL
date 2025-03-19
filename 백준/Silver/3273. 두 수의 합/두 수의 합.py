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
