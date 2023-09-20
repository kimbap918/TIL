import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = list(int(input()) for _ in range(N))
X.sort() # 이분탐색을 위한 정렬
start, end = 1, X[-1] # 시작 = 최소, 끝 = 최대

def binary_search(arr, start, end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        current = arr[0]
        cnt = 1
        # 집으 맨 앞 부터 차례로 순회
        for i in range(1, len(arr)):
            # 순회하는 집이 마지막 저장된 집 위치+mid보다 크면?
            # 인접한 공유기 중 거리를 최대한으로 설치 가능함
            if arr[i] >= current + mid:
                cnt += 1
                current = arr[i]
        # 공유기의 설치 수가 공유기 개수를 넘거나 같으면
        if cnt >= C:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res

print(binary_search(X, start, end))
