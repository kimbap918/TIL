## 파이썬 팩토리얼(백준 BOJ 10872) 

<br>

## 문제

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

<br>

## 출력

첫째 줄에 N!을 출력한다.

<br>

## 예제 입력 1

```
10
```

## 예제 출력 1 

```
3628800
```

## 예제 입력 2

```
0
```

## 예제 출력 2

```
1
```

<br>

## 📝 풀어보기

처음에는 for문으로 풀었다.

[For]

``` python
# factorial = 5! 1x2x3x4x5
N = int(input())
a = 1
for i in range(1, N+1):
  a *= i
print(a)
```

<br>

문제를 다시 보니 재귀함수로 푸는데에 의미가 있는것 같아 다시 풀었다.

[Recursive]

``` python
def factorial(N):
  if N == 1:
    return 1
  else :
    return N * factorial(N-1)

N = int(input())
print(factorial(N))
```

코드를 보면 함수 내에서 다시 함수를 부르고 값을 리턴하고있다.

만약 5를 입력했다면 순서대로 아래와 같은 연산과정을 거쳐서 120이 나왔을것이다.

``` python
# N * factorial(N-1) 
5 * factorial(4) # 5 곱하기 factorial(4)를 호출
# factorial(4)가 호출됨
4 * factorial(3) # 4 곱하기 factorial(3)을 호출
# factorial(3)이 호출됨
3 * factorial(2) # 3 곱하기 factorial(2)를 호출
# factorial(2)가 호출됨
2 * factorial(1) # 2 곱하기 factorial(1)을 호출
1 return 1 # 1이므로 1을 리턴

1 * 2 = 2 # 리턴된 1에 2를 곱함
2 * 3 = 6 
6 * 4 = 24
24 * 5 = 120
```

