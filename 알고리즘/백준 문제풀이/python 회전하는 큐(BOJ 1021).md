## 파이썬 회전하는 큐(백준 BOJ 1021)

<br>

## 문제

지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

<br>

## 출력

첫째 줄에 문제의 정답을 출력한다.

<br>

## 예제 입력 1 

```
10 3
1 2 3
```

## 예제 출력 1

```
0
```

## 예제 입력 2 

```
10 3
2 9 5
```

## 예제 출력 2

```
8
```

## 예제 입력 3

```
32 6
27 16 30 11 6 23
```

## 예제 출력 3

```
59
```

## 예제 입력 4 

```
10 10
1 6 3 2 7 9 8 4 10 5
```

## 예제 출력 4

```
14
```

<br>

## 📝 풀어보기

📌 deque를 사용하기 위해 from collections import deque 라이브러리를 가져온다.

queue의 크기 N, 뽑아내려고 하는 수의 개수  M을 입력받고 뽑아내려는 수의 위치를 입력받는다.

그리고 queue에 1부터 N까지의 수를 저장한다.

``` python
from collections import deque
import sys
input = sys.stdin.readline
# queue의 크기 N, 뽑아내려고 하는 수의 개수 M
N, M = map(int, input().split())
pos = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])
```

<br>

📌 pos의 요소를 순회하면서 모두 뽑아낼때까지 반복한다.

queue의 첫번째 요소가 뽑아내려는 값과 같으면 값을 뽑아내고 반복을 종료한다.

그외에 인덱스의 값이 큐를 반으로 나눈것 보다 작다면 왼쪽의 값이므로 왼쪽의 값을 뽑아내고 queue의 오른쪽에 삽입하면서 카운트를 늘린다.

인덱스의 값이 큐를 반으로 나눈것 보다 크다면 오른쪽의 값이므로 오른쪽의 값을 뽑아내고 왼쪽에 삽입하면서 카운트를 늘린다.

최종 카운트를 출력한다.

``` python
cnt = 0
for i in pos: # 위치 하나씩마다 반복하기
    while True: # 뽑을때까지 반복하기
        if queue[0] == i: # 큐의 첫 인덱스가 뽑아내려는 숫자와 같다면
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2: # 인덱스 값이 큐를 반으로 나눈것보다 작으면?
                while queue[0] != i: # 2번 실행
                    queue.append(queue.popleft())
                    cnt += 1
            else: # 큐를 반으로 나눈 값 보다 크면 
                while queue[0] != i: # 3번 실행
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)
```

<br>

#### 전체 코드

``` python
# 1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
from collections import deque
import sys
input = sys.stdin.readline
# queue의 크기 N, 뽑아내려고 하는 수의 개수 M
N, M = map(int, input().split())
pos = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])

cnt = 0
for i in pos: # 위치 하나씩마다 반복하기
    while True: # 뽑을때까지 반복하기
        if queue[0] == i: # 큐의 첫 인덱스가 뽑아내려는 숫자와 같다면
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2: # 인덱스 값이 큐를 반으로 나눈것보다 작으면?
                while queue[0] != i: # 2번 실행
                    queue.append(queue.popleft())
                    cnt += 1
            else: # 큐를 반으로 나눈 값 보다 크면 
                while queue[0] != i: # 3번 실행
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)
```



