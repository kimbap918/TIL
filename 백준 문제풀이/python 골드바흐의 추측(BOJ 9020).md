## 파이썬 골드바흐의 추측(백준 BOJ 9020)

<br>

## 문제

1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

<br>

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

<br>

## 출력

각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

<br>

## 제한

- 4 ≤ n ≤ 10,000

<br>

## 예제 입력 1

```
3
8
10
16
```

## 예제 출력 1

```
3 5
5 5
5 11
```

<br>

## 📝 문제풀기

에라토스테네스의 체를 이해하고 나니 생각보다 쉽게 풀수 있었다.

📌 먼저, 이 문제의 제한값인 10000을 변수로 선언하고 소수를 분별할 리스트를 2개 만든다. 0과 1은 소수가 아니므로 False로 선언한다. 수업에서 배운 List Comprehention이 생각나서 이번에 리스트 값을 넣을때 사용해봤다.

``` python
N = 10000
array1 = []
array2 = []
# List Comprehention
# [변수를 활용한 값 / for 사용할 변수 이름 in 순회할 수 있는 값 / + 조건문]
[array1.append(i) for i in range(N+1) if True]
array1[0], array1[1] = False, False
```

<br>

📌 에라토스테네스의 체를 사용했다.

10000까지 숫자가 담긴 리스트에 i*j++ 의 값에 해당하는 숫자를 False처리한다. 그리고 array2에 False가 아닌 값(소수)을 담는다.

``` python
for i in range(2, int(N**0.5)+1):
    if array1[i]:
        j = 2
        while i*j <= N:
            array1[i*j] = False
            j += 1
[array2.append(i) for i in range(len(array1)) if array1[i] != False]
```

<br>

📌 이제 입력 부분이다.

테스트 케이스 T를 선언하고 입력할 값n과 n을 나눈 몫인 half를 선언한다. 여기서 half는 두 소수 차이가 가장 작은것을 판별하기 위해 큰 수를 먼저 꺼내려고 사용했다. 

``` python
T = int(input())
for i in range(T):
    n = int(input())# 만약 10이면
    half = n // 2 # 5
    for j in range(half, 1, -1): # 5 4 3 2 1
      	# 10 - 5 = 5 는 소수? and 5 는 소수? o
        # 10 - 4 = 6 은 소수? and 4 는 소수? x
        # ... 
        if (n - j in array2) and (j in array2):
          	# 5, 5
            print(j, n-j)
            break
```

<br>

#### 전체코드

``` python
N = 10000
array1 = []
array2 = []
[array1.append(i) for i in range(N+1) if True]
array1[0], array1[1] = False, False

for i in range(2, int(N**0.5)+1):
    if array1[i]:
        j = 2
        while i*j <= N:
            array1[i*j] = False
            j += 1
[array2.append(i) for i in range(len(array1)) if array1[i] != False]

T = int(input())
for i in range(T):
    n = int(input())
    half = n // 2
    for j in range(half, 1, -1):
        if (n - j in array2) and (j in array2):
            print(j, n-j)
            break
```

