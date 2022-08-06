## 파이썬 N번째 큰 수(백준 BOJ 2693)

<br>

## 문제

배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.

배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

<br>

## 입력

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 배열 A의 원소 10개가 공백으로 구분되어 주어진다. 이 원소는 1보다 크거나 같고, 1,000보다 작거나 같은 자연수이다.

<br>

## 출력

각 테스트 케이스에 대해 한 줄에 하나씩 배열 A에서 3번째 큰 값을 출력한다.

<br>

## 예제 입력 1

```
4
1 2 3 4 5 6 7 8 9 1000
338 304 619 95 343 496 489 116 98 127
931 240 986 894 826 640 965 833 136 138
940 955 364 188 133 254 501 122 768 408
```

## 예제 출력 1

```
8
489
931
768
```

<br>

## 📝 풀어보기

처음에 단순 for문으로 풀었지만 시간초과가 걸렸다.

최소힙을 참고하여 문제를 풀었다.



📌 `heapq` 와  `sys` 를 import한다. 빠른 입력과 heap의 사용을 위해서 가져왔다. 그리고 반복할 횟수와 N번째로 큰 값을 찾기위한 변수 `N` 을 선언하고 힙 리스트를 하나 만든다.

``` python
import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []
```

<br>

📌  N번동안 반복하면서 값을 비교할 수를 입력받는다.

heap이 아닐 경우 heap에 입력한 숫자를 추가하고, 그외에 힙의 첫번째요소와 입력되어 순회하는 num값을 비교하여 num보다 작을 경우에 heap에 num을 푸시하고 제일 작은 요소를 pop한다.

이렇게 for문을 따라 N번 반복하면 결국 heap의 첫번째 요소엔 N번째로 큰 수가 남게된다.

``` python
for _ in range(N): # N번동안 반복 
    nums = list(map(int, input().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num) # heap에 num값을 푸시
    else:
        for num in nums:
            if heap[0] < num: # 힙 리스트의 첫번째 요소가 num보다 작을 경우
                heapq.heappush(heap, num) # num을 heap에 푸시
                heapq.heappop(heap) # heap의 제일 작은 요소를 팝
print(heap[0])
```

<br>

#### 전체 코드

``` python
import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N): # N번동안 반복 
    nums = list(map(int, input().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num) # heap에 num값을 푸시
    else:
        for num in nums:
            if heap[0] < num: # 힙 리스트의 첫번째 요소가 num보다 작을 경우
                heapq.heappush(heap, num) # num을 heap에 푸시
                heapq.heappop(heap) # heap의 제일 작은 요소를 팝
print(heap[0])
```

