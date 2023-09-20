## 파이썬 소수 구하기(백준 BOJ 1929)

시간초과를 해결하지 못해서 몇번이나 개선했던 문제다.😭

<br>

## 문제

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

<br>

## 출력

한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

<br>

## 예제 입력 1 

```
3 16
```

## 예제 출력 1

```
3
5
7
11
13
```

<br>

## 📝 풀어보기

📌 N 의 범위가 1,000,000에 제한시간이 2초인 문제였기 때문에 내가 아는 선에서 불필요한 코드를 줄이고 개선하려고 했다.

 `sys.stdin.readline()`를 사용하기 위해 sys를 import했다.

``` python
import sys

M, N = map(int, sys.stdin.readline().split())
```

<br>

📌 에라토스테네스의 체 방식을 이용해 2부터 i의 제곱근까지만 수행하고 소수가 아닐 경우에 False로 바꾸고 break한다. 소수일 경우에는 M이상의 소수만 추가해서 출력하도록 했다.

``` python
# 에라토스테네스의 체 방식 사용
for i in range(2, N+1): # 2부터 N+1의 범위까지 탐색
    check = True
    for j in range(2, int(i**0.5)+1): # 2부터 i의 제곱근까지만 수행
        if i % j == 0: # 소수가 아닐 경우
            check = False
            break
    if check:   # 소수일경우
        if i >= M: # M 이상의 소수만 추가
            print(i)
```

<br>

지난번에 소수 풀이때 썼던 코드인데 에라토스테네스의 체 방식을 사용하더라도 반복적인 for문과 리스트를 사용하면 속도가 많이 떨어지는걸 느꼈다. 덕분에 많이 배운것 같다.

``` python
M = int(input()) # 최소값 
N = int(input()) # 최대값
A = [] # 범위 내의 소수를 담을 리스트
B = 0 # 합계를 담을 변수 

# 에라토스테네스의 체
for i in range(2, N+1): # 2부터 최대값+1의 범위까지
    check = True
    for j in range(2, int((i**0.5)+1)): # 최대값의 제곱근까지만 탐색
        if i%j == 0:
            check = False
    if check:
        if i >= M: # 도출된 소수가 최소값인 M보다 클 경우에만 삽입
            A.append(i)

for k in range(len(A)): # 리스트 A의 합계
    B += A[k]  

if A != []: # 리스트가 비어있지 않을 경우
    print(B)
    print(A[0])
else: # 비어있는 경우
    print(-1)
```

<br>

#### 전체 코드

``` python
import sys

M, N = map(int, sys.stdin.readline().split())

# 에라토스테네스의 체 방식 사용
for i in range(2, N+1): # 2부터 N+1의 범위까지 탐색
    check = True
    for j in range(2, int(i**0.5)+1): # 2부터 i의 제곱근까지만 수행
        if i % j == 0: # 소수가 아닐 경우
            check = False
            break
    if check:   # 소수일경우
        if i >= M: # M 이상의 소수만 추가
            print(i)

```

