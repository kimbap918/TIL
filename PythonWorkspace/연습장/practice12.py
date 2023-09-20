import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])

# 시간종료순으로 정렬, 오름차순
arr.sort(key=lambda x : (x[1], x[0]))
cnt = 0
end = 0
for s, e in arr:
    if s > end:
        end = e
        cnt += 1
print(cnt)
# for i in range(len(arr)-1):
#     if arr[i][1] == arr[i+1][0] and arr[i][2] < arr[i+1][2]:
#         continue
#     for j in range(arr[i][0], arr[i][1]):
#         if (arr[i+1][0] == j or arr[i+1][1] == j) and arr[i][2] > arr[i+1][2]:
#             arr[i][2] = max_num
#     if arr[i][2] == max_num:
#         continue
#     ans.append(arr[i])

# print(max_num)
# print(ans)