## 파이썬 최대 힙(BOJ 11279)

우선순위 큐(Heap, Priority Queue)에 관해

<br>

## 문제

널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.

<br>

## 입력

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 231보다 작다.

<br>

## 출력

입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

<br>

## 예제 입력 1 

```
13
0
1
2
0
0
3
2
1
0
0
0
0
0
```

## 예제 출력 1 

```
0
2
1
3
2
1
0
0
```

<br>

## 📝 풀어보기

<br>

이 문제를 풀어보기 전에 우선순위 큐(Heap, Priority Queue)에 대해 조금 알아봐야한다.

우리가 1부터 10까지 숫자를 저장하는 자료구조를 구현하는데, 숫자가 랜덤으로 삽입된다면?

숫자가 클 수록 우선순위가 높다고 가정했을때, 삽입된 값을 빼낸다면 10, 9, 8, 7 ... 1순으로 추출된다. 이것은 **최대 힙(Max Heap)**이라 부른다.

숫자가 작을 수록 우선순위가 높다고 가정했을때, 삽입된 값을 빼낸다면 1, 2, 3, 4 ... 10순으로 추출된다. 이것은 **최소 힙(Min Heap)**이라 부른다.

<br>

이러한 우선순위 큐를 구현할 때의 특징은 다음과 같다.

1.  완전 이진 트리(Complete Binary Tree)를 기반으로한 자료구조로, 부모 노드가 자식 노드보다 큰 값을 가지는 Max Heap과, 부모 노드가 자식 노드보다 작은 값을 가지는 Min Heap으로 나뉜다.
2. 일반적으로 배열로 구현한다.
3. 반 정렬 상태를 유지한다.(느슨한 정렬)

<br>

아래 그림처럼 1차원 배열에 기록될 때, 부모(100)의 현재 인덱스가 n이라면 왼쪽 자식 노드(19)는 n*2, 오른쪽 자식 노드(36)은 n*2+1에 위치된다.

![heap](https://user-images.githubusercontent.com/75712723/232426382-149dd0af-1c9c-4337-92af-1d8507cc9efb.png)

힙에 자료를 push할 경우에 맨 끝 노드부터 채워지며, 맨 끝에 push한 뒤에 부모 노드를 검사하며 부모 노드보다 크다면 위치를 바꾸며 거슬러 올라가는데, 이를 heapify라고 한다.

pop을 할 경우, 무조건 뿌리 노드를 추출한다. 뿌리 노드에 최소, 최대값이 들어있기 때문이다.

그리고 추출하고 빈 뿌리 노드에 맨 마지막에 넣었던 노드를 가져온다. 그리고 heapify의 방향만 바꿔 실행한다.

아래는 최대힙을 구현한 코드다.

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

heap = [0]
capacity = 0

# push를 하는 함수
def push(heap, n):
    global capacity
    # heap 의 자리가 부족할경우 배열을 2배로 늘림
    if len(heap)-1 == capacity:
        heap += [0]*len(heap)

    capacity += 1
    heap[capacity] = n

    # heapify
    tn = capacity
    while(tn > 1):
        if heap[tn] > heap[tn//2]:
            temp = heap[tn]
            heap[tn] = heap[tn//2]
            heap[tn//2] = temp
            tn//=2
        else:
            break
    return heap

# pop을 하는 함수
def pop(heap):
    global capacity
    if capacity == 0:
        return 0
    p = heap[1]
    heap[1] = heap[capacity]
    heap[capacity] = 0

    tn = 1
    # push의 heapify의 방향을 바꿔서 실행
    while(capacity > tn*2):
        if heap[tn*2] == 0 and heap[tn*2+1] == 0:
            break
        if heap[tn] < max(heap[tn*2], heap[tn*2+1]):
            temp = heap[tn]
            if heap[tn*2] > heap[tn*2+1]:
                heap[tn] = heap[tn*2]
                heap[tn*2] = temp
                tn*=2
            else:
                heap[tn] = heap[tn*2+1]
                heap[tn*2+1] = temp
                tn = tn*2+1
        else:
            break
    capacity -= 1
    return p

for i in range(int(input())):
    x = int(input())
    if x: # true
        heap = push(heap, x)
    else: # false
        print(pop(heap))
```

<br>

그리고 파이썬에서는 이 heap을 사용할 수 있는 heapq모듈이 있다.

아래는 heapq 모듈을 사용해서 위와 같은 최대 힙을 구하는 코드다.

``` python
import sys
import heapq as hq
input = sys.stdin.readline

heap = []
for i in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)
```

