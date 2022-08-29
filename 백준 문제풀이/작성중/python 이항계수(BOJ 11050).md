## 파이썬 이항계수 1(백준 BOJ 11050)

<br>

## 문제

자연수 N\(N\)과 정수 K\(K\)가 주어졌을 때 이항 계수 (NK)\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 N\(N\)과 K\(K\)가 주어진다. (1 ≤ N\(N\) ≤ 10, 0 ≤ K\(K\) ≤ N\(N\))

<br>

## 출력

 (NK)\(\binom{N}{K}\)를 출력한다.

<br>

## 예제 입력 1

```
5 2
```

## 예제 출력 1

```
10
```

<br>

## 📝 풀어보기

``` python
# 이항 계수(Binomial Coefficient)
# 조합론에서 등장하는 개념으로 주어진 크기 집합에서 원하는 개수만큼 순서 없이 뽑는 조합의 가짓수

# 1. N * ... * 1을 총 K번 진행
# 2. K! 계산
# 3. 1번의 결과를 2번의 결과로 나눔

# Factorial 계산하는 함수
def factorial(K):
    if K < 2:
        return 1
    else:
        return K * factorial(K-1)
    
# 입력
N, K = map(int, input().split())

# N * N-1 * ...
num1 = 1
for i in range(K):
    num1 *= N-i

# K!
num2 = factorial(K)

# N * N-1 * ... // K!
print(num1 // num2)
```

