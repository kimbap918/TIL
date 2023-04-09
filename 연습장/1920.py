# import sys
# input = sys.stdin.readline

# N = int(input())
# arr1 = set(map(int, input().split()))
# M = int(input())
# arr2 = list(map(int, input().split()))

# for num in arr2:
#     print(1) if num in arr1 else print(0)


# 이진탐색
import sys
input = sys.stdin.readline
N = int(input())
# 이분탐색을 위해 집합 arr1을 먼저 정렬
arr1 = sorted(map(int, input().split()))
M = int(input())
arr2 = map(int, input().split())

def binary(num, arr, start, end):
    if start > end:
        return 0
    # 시작과 끝 지점을 이용해서 중간 지점의 인덱스를 구한다.
    mid = (start+end)//2
    # 중간지점의 값과 arr2의 요소를 비교한다.
    # 동일값이몇 리턴, 값이 크면 중간보다 윗부분, 값이 작으면 중간보다 작은 부분에서 탐색
    if num == arr[mid]:
        return 1
    # arr2의 요소가 중간보다 작으면
    elif num < arr[mid]:
        # 작은쪽(왼쪽)을 탐색
        return binary(num, arr, start, end-1)
    # arr2의 요소가 중간보다 크면
    else:
        # 큰쪽(오른쪽)을 탐색
        return binary(num, arr, start+1, end)

for num in arr2:
    # 시작과 끝 지점의 인덱스를 지정한다. 
    start = 0
    end = len(arr1)-1
    print(binary(num, arr1, start, end))