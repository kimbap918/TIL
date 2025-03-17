import sys
input = sys.stdin.readline

def binary_search(arr, tar, start, end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            end = mid - 1
        else:
            start = mid + 1
    return None


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
x = list(map(int, input().split()))

for i in x:
    res = binary_search(arr, i, 0, N-1)
    if res != None:
        print("Yes", end=' ')
    else:
        print("No", end=' ')


