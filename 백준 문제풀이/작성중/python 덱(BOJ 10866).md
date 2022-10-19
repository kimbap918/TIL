## 파이썬 덱 (백준 BOJ 10866)

<br>

## 문제

정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

- push_front X: 정수 X를 덱의 앞에 넣는다.
- push_back X: 정수 X를 덱의 뒤에 넣는다.
- pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 덱에 들어있는 정수의 개수를 출력한다.
- empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
- front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

<br>

## 입력

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

<br>

## 출력

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

<br>

## 예제 입력 1

```
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
```

## 예제 출력 1

```
2
1
2
0
2
1
-1
0
1
-1
0
3
```

## 예제 입력 2

```
22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back
```

## 예제 출력 2 복사

```
-1
-1
-1
-1
1
1
2
2
333
10
10
333
20
1234
1234
20
```

<br>

## 📝 풀어보기

``` python
from collections import deque
import sys

d = deque()
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        d.appendleft(command[1])
    elif command[0] == "push_back":
        d.append(command[1])
    elif command[0] == "pop_front":
        if d:
            print(d[0])    
            d.popleft()
        else:
            print("-1")
    elif command[0] == "pop_back":
        if d:
            print(d[len(d) - 1])    
            d.pop()
        else:
            print("-1")
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif command[0] == "back":
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")
```

