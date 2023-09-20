## 파이썬 스택(백준 BOJ 10828)

<br>

## 문제

정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

- push X: 정수 X를 스택에 넣는 연산이다.
- pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 스택에 들어있는 정수의 개수를 출력한다.
- empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
- top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

<br>

## 입력

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

<br>

## 출력

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

<br>

## 예제 입력 1

```
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
```

## 예제 출력 1

```
2
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
7
pop
top
push 123
top
pop
top
pop
```

## 예제 출력 2

```
-1
-1
123
123
-1
-1
```

<br>

## 📝 풀어보기

📌 스택 역할을 할 리스트를 생성한다. 연산횟수 N을 생성하고 N만큼 반복하면서 연산을 입력받는다.

여기서 push 명령어는 뒤에 숫자가 붙으므로, 연산을 split()으로 받아 명령어와 숫자를 각각 분리할 수 있게 한다.

이후로는 주석의 조건에 맞게 if문을 구성한다.

``` python
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
input = sys.stdin.readline
stack = []
N = int(input())

for _ in range(N):
    word = input().split()
    command = word[0]

    if command == "push":
        val = word[1]
        stack.append(val)
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
```

