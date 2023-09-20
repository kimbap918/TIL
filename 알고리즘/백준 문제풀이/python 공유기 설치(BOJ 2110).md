## 파이썬 공유기 설치(BOJ 2110)

<br>

## 문제

도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

<br>

## 출력

첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

<br>

## 예제 입력 1

```
5 3
1
2
8
4
9
```

## 예제 출력 1 

```
3
```

<br>

## 힌트

공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.

<br>

## 📝 풀어보기

<br>

N개의 집에 C개만큼의 공유기를 설치하되, 인접한 두 공유기 사이의 거리를 최대로 띄워야하는 문제다.

<br>

N개의 집의 개수, C개의 공유기 수를 입력받는다.

집의 좌표 x를 리스트 X에 담아 저장하고, 이분탐색을 위해 정렬을 한다.

시작점을 1, 끝점을 리스트의 최대값인 마지막 요소를 저장한다.  

``` python
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = list(int(input()) for _ in range(N))
X.sort() # 이분탐색을 위한 정렬
start, end = 1, X[-1] # 시작 = 최소, 끝 = 최대
```

<br>

이분 탐색 함수를 만든다.

계산된 결과값을 출력하기 위해 res를 만들어두고

while문으로 반복하면서, 이분 탐색을 위한 중간지점(시작+끝)//2, 공유기를 설치하고 현재 위치, 공유기의 설치 개수를 저장해둔다.

for문으로 집의 맨 앞부터 차례로 순회하면서 현재 순회하는 집의 좌표값이 저장해둔 집의 위치값+중간지점 보다 크거나 같으면 공유기를 설치하고 현재 위치를 갱신한다.

공유기 설치대수가 공유기의 개수보다 크거나 같아지면, 시작지점을 중간값+1로 갱신하고 결과값을 중간값으로 갱신한다.

그외엔 끝 지점을 중간값 -1로 갱신하고 반복이 종료되면 결과값을 반환한다.

``` python
def binary_search(arr, start, end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        current = arr[0]
        cnt = 1
        # 집의 맨 앞 부터 차례로 순회
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
```

<br>

#### 전체코드

``` python
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
```



