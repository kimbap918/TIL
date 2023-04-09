import sys
input = sys.stdin.readline

N = int(input())
arr1 = sorted(map(int, input().split()))
M = int(input())
arr2 = map(int, input().split())

def binary_search(num, arr, start, end):
    # 시작보다 끝이 작으면
    if start > end:
        return 0

    mid = (start+end) // 2

    if num == arr[mid]:
        return 1
    elif num < arr[mid]:
        return binary_search(num, arr, start, mid-1)
    else:
        return binary_search(num, arr, mid+1, end)

for num in arr2:
    start = 0
    end = len(arr1)-1
    print(binary_search(num, arr1, start, end))