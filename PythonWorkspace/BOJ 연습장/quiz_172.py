n = int(input())
arr = list(map(int, input().split()))
max_sum = [arr[0]] # 비교를 위한 arr값 입력

for i in range(len(arr) -1): # 0부터 arr-1까지
    max_sum.append(max(max_sum[i] + arr[i+1], arr[i+1])) # sum[i]+arr[i+1]과 arr[i+1]중 큰 값을 비교 후 추가
print(max(max_sum)) # 추가된 값들 중 최대값 출력