## 파이썬 스택 수열(BOJ 1874)

<br>

## 문제

스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

<br>

## 입력

첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

<br>

## 출력

입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

<br>

## 예제 입력 1 

```
8
4
3
6
8
7
5
2
1
```

## 예제 출력 1

```
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
```

## 예제 입력 2

```
5
1
2
5
3
4
```

## 예제 출력 2 복사

```
NO
```

<br>

## 힌트

1부터 n까지에 수에 대해 차례로 [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.

<br>

## 📝 풀어보기

📌 연산 횟수 N을 입력받고, 스택 stack, 연산자를 담을 oper, 카운트 cnt, 연산 가능 여부를 판별할 temp를 생성한다.

``` python
import sys
input = sys.stdin.readline
N = int(input())
stack = []
oper = []
cnt = 1
temp = True
```

<br>

📌 N만큼 반복하면서 연산 명령을 입력받는다.

cnt 보다 명령어의 값이 크면 append로 추가해야한다. 이 때, 마지막으로 입력된 숫자보다 작은 값은 append되지 않기때문에 cnt보다 큰 값이 항상 담길수 있도록 한다. stack에 추가될때 oper에도 연산자를 추가해준다.

``` python
for _ in range(N):
    command = int(input())
    if cnt <= command: # cnt 보다 명령어가 크면 추가
        for i in range(cnt, command+1): # cnt이후의 수
            stack.append(cnt)
            oper.append('+')
            # print("cnt:"+str(cnt))
            # print("stack:"+str(stack))
            cnt += 1 # cnt 증가
```

<br>

📌 stack의 마지막 값이 입력값과 같다면 pop명령어로 제거한다. oper에는 - 연산자를 추가한다.

그 외에는 연산이 불가능한 경우이므로 temp를 False로 바꾼다.

temp의 결과값이 False인 경우 NO를 출력하고 그 외엔 oper에서 연산자를 하나씩 꺼내서 출력한다.

``` python
    if stack[-1] == command: # stack의 끝이 입력숫자와 같으면
        stack.pop() # 빼준다
        oper.append('-') # - 추가
        # print("stack:"+str(stack))
    else: # 그외(연산불가)
        temp = False 

if temp == False:
    print('NO')
else:
    for i in oper:
        print(i)
```



``` python
import sys
input = sys.stdin.readline
N = int(input())
stack = []
oper = []
cnt = 1
temp = True

for _ in range(N):
    command = int(input())
    if cnt <= command: # cnt 보다 명령어가 크면 추가
        for i in range(cnt, command+1): # 중복숫자는 안나오므로 cnt이후의 수
            stack.append(cnt)
            oper.append('+')
            # print("cnt:"+str(cnt))
            # print("stack:"+str(stack))
            cnt += 1 # cnt 증가

    if stack[-1] == command: # stack의 끝이 입력숫자와 같으면
        stack.pop() # 빼준다
        oper.append('-') # - 추가
        # print("stack:"+str(stack))
    else: # 그외(연산불가)
        temp = False 

if temp == False:
    print('NO')
else:
    for i in oper:
        print(i)

```

