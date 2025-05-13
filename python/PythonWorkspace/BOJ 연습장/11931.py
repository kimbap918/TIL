import sys
input = sys.stdin.readline

def quick(arr):
    stack = [(0, len(arr)-1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = partition(arr, start, end)
        stack.append((start, pivot-1))
        stack.append((pivot+1, end))


def partition(arr, start, end):
    pivot = arr[start]
    low = start+1
    high = end

    while True:
        while low <= high and arr[low] <= pivot:
            low += 1
        while low <= high and arr[high] >= pivot:
            high -= 1

        if low > high:
            break

        arr[low], arr[high] = arr[high], arr[low]


    arr[start], arr[high] = arr[high], arr[start]
    return high


N = int(input())
nums = [int(input()) for _ in range(N)]
quick(nums)

for num in reversed(nums):
    print(num)
