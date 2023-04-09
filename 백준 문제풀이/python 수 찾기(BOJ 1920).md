## 파이썬 수 찾기(BOJ 1920)

<br>

## 문제

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

<br>

## 출력

M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

<br>

## 예제 입력 1 

```
5
4 1 5 2 3
5
1 3 7 9 5
```

## 예제 출력 1

```
1
1
0
0
1
```

<br>

## 📝 풀어보기

### 이분 탐색?

이분 탐색(Binary Search)는 **오름차순 혹은 내림차순으로 정렬된 수열**에서 검색하는 알고리즘이다. 선형 탐색보다 훨씬 빠르게 탐색할 수 있다는 장점이 있다. 시간복잡도는 탐색할 범위를 절반으로 줄여서 탐색하므로 **O(logn)**이다.

이분 탐색의 방법

1. 배열(arr)의 **가운데 요소의 인덱스**를 mid으로 정한다.
2. arr[mid]의 값이 찾고자 하는 요소와 같다면 검색완료
3. arr[mid]의 값이 찾는 값보다 크다면 **left ~ mid** 사이를 탐색한다.
4. arr[mid]의 값이 찾는 값보다 작다면 **mid ~ right** 사이를 탐색한다.

<br>

문제에 필요한 N, N의 배열, M, M의 배열을 입력받는다. 이분탐색을 위해 arr1을 정렬시킨다. 

``` python
import sys
input = sys.stdin.readline

N = int(input())
arr1 = sorted(map(int, input().split()))
M = int(input())
arr2 = map(int, input().split())
```

<br>

이분 탐색을 구현한다.

먼저 M의 배열 arr2에서 요소값을 순회하면서, 시작점과 끝지점을 지정해두고, 함수를 실행시킨다.

``` python
for num in arr2:
    start = 0
    end = len(arr1)-1
    print(binary_search(num, arr1, start, end))
```

<br>

시작점+끝점 // 2를 mid에 저장해둔다.

`arr1[mid]` 가 num과 같다면 찾는 숫자가 있는것이므로 1을 반환,

num이 arr[mid] 보다 작으면 mid-1 해서 중간값보다 왼쪽을 탐색한다.

num이 arr[mid] 보다 크면 mid+1 해서 중간값보다 오른쪽을 탐색한다.

``` python
def binary_search(num, arr, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if num == arr[mid]:
        return 1
    elif num < arr[mid]:
        return binary_search(num, arr, start, mid-1)
    else:
        return binary_search(num, arr, mid+1, end)
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

N = int(input())
arr1 = sorted(map(int, input().split()))
M = int(input())
arr2 = map(int, input().split())

def binary_search(num, arr, start, end):
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
```

