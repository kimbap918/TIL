## 파이썬 프린터 큐(백준 BOJ 1966)

<br>

## 문제

여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

<br>

## 입력

첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

<br>

## 출력

각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

<br>

## 예제 입력 1 

```
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
```

## 예제 출력 1

```
1
2
5
```

<br>

## 📝 풀어보기

📌 테스트 케이스의 수를 입력받는다.

N은 문서의 개수, M은 queue에서 몇번째로 놓여져있는지를 나타낸다.

queue에 N개만큼 우선순위가 담긴 문서를 입력받고 count 변수를 생성한다.

``` python
from collections import deque
import sys
# 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
# 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
# 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
input = sys.stdin.readline
TC = int(input())

for i in range(TC):
    # N: 문서의 개수, M: queue에서 몇번째로 놓여있는지
    # M이 남은 큐 중에서 가장 큰수가 될때까지 검사
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
```

<br>

📌 queue의 값이 빌때까지 반복하면서 큐의 최소 우선순위값을 best에 저장하고 맨 왼쪽의 값을 빼서 front에 저장한다. 큐의 값이 빠질때마다 M을 1씩 뺀다.

만약, 뽑은 숫자(front)가 제일 큰 숫자(best)면 count를 1 증가시키고, M이 음수이면 count를 출력하고 종료한다.

뽑은숫자가 제일 큰 숫자가 아닌경우, 빼낸 숫자를 맨 뒤에 붙이고 큰 숫자가 뽑힐때까지 앞을 빼고, 뒤에 붙이면서 반복한다. 이 때, M이 음수가 되면 큐 길이 -1값을 다시 M에 저장한다. 

``` python
while queue:
        best = max(queue) # 큐의 최고 우선순위값 저장
        front = queue.popleft() # 맨 왼쪽의 값을 뺌
        # print(best, front, M)
        # print(queue)
        M -= 1 # M을 -1 이동

        if best == front: # 뽑은 숫자가 제일 큰 숫자면
            count += 1 # 하나가 배출되었기 때문에 카운트 증가
            if M < 0: 
                print(count) 
                break
        else:
            queue.append(front) # 빼낸 숫자를 맨 뒤에 붙인다
            # print(queue) 
            if M < 0: # 음수로 떨어지면
                M = len(queue)-1 # 큐 길이 -1 
```

<br>

#### 전체코드

``` python
from collections import deque
import sys
# 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
# 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
# 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
input = sys.stdin.readline
TC = int(input())

for i in range(TC):
    # N: 문서의 개수, M: queue에서 몇번째로 놓여있는지
    # M이 남은 큐 중에서 가장 큰수가 될때까지 검사
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        best = max(queue) # 큐의 최고 우선순위값 저장
        front = queue.popleft() # 맨 왼쪽의 값을 뺌
        # print(best, front, M)
        # print(queue)
        M -= 1 # M을 -1 이동

        if best == front: # 뽑은 숫자가 제일 큰 숫자면
            count += 1 # 하나가 배출되었기 때문에 카운트 증가
            if M < 0: 
                print(count) 
                break
        else:
            queue.append(front) # 빼낸 숫자를 맨 뒤에 붙인다
            # print(queue) 
            if M < 0: # 음수로 떨어지면
                M = len(queue)-1 # 큐 길이 -1 
```

