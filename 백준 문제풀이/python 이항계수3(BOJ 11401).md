## 파이썬 이항계수3(백준 BOJ 11401)

## 문제

자연수 �\(N\)과 정수 �\(K\)가 주어졌을 때 이항 계수 (��)\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 �\(N\)과 �\(K\)가 주어진다. (1 ≤ �\(N\) ≤ 4,000,000, 0 ≤ �\(K\) ≤ �\(N\))

## 출력

 (��)\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 출력한다.

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

우선 이 문제는 이항계수 2(BOJ 11051)에서 N과 K의 값이 4,000,000까지 늘어났다.

기존에 풀었던 문제의 코드를 한번 살펴보자.

``` python
from math import factorial
n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)
```

<br>

### 이항계수

**이항계수(Binomial Coeffieient)**는 조합론에서 등장하는 개념으로, 주어진 크기 집합에서 원하는 개수만큼 순서 없이 뽑는 조합의 가짓수를 말한다. 예를 들자면 N = {a, b, c}  집합 N에서 2개를 뽑는 조합은 {a, b}, {a, c}, {b, c}로 총 3개다.

이항계수를 구하는 식은 **nCk = n! / (k! \* (n-k)!)**다.

이항계수2 에서 문제를 푼 방식은 바로 위의 식을 이용한것인데, 위의 식의 가장 큰 문제는 부분문제의 중복에 있다.

https://nulls.co.kr/codeit/386 

재귀함수를 사용하면서 위와 같이 문제를 풀기위한 부분문제가 너무 중복되어서 시간을 잡아먹는것이다.

<br>

### 모듈러 연산(나머지 연산)

문제를 해결하기 위한 이론을 하나씩 알아보자.

17을 5로 나눈 나머지는 2다. 17 mod 5 = 2, 이때 17과 2는 서로 동치이며(mod 5에서), 17 ≡ 2 (mod 5)로 나타낸다.

<br>

### 모듈러 연산의 분배법칙

모듈러 연산의 분배법칙에 대해 알아보자.

1. (A + B) % p = ((A % p) + (B % p)) % p
2. (A - B) % p = ((A % p) - (B % p) + p) % p
3. (A x B) % p = ((A % p) x (B % p)) % p

나눗셈에 대해서는 분배법칙이 성립하지 않는다. 

여기서 나눗셈에 대한 분배법칙이 성립하지 않는것을 해결하기 위해, 곱셈에 대한 분배법칙을 활용한다.

<br>

### 모듈러 연산의 성질

정수 a 와 소수 p가 주어졌을 때, `a^p ≡ a (mod p)`는 **좌변의 a를 p로 나눈 나머지와**, **우변의 a^p를 p로 나눈 나머지가 동일하다**는 성질을 나타낸다. 즉, 2^3을 3으로 나눈 나머지와, 2를 3으로 나눈 나머지가 같다.

그럼 이 식의 양변을 a^2 로 나눠보자.

**a^p-2 ≡ a^-1 (mod p) (a는 0이 아님)**

<br>

### 모듈러 연산의 역원(Inverse)

`역원(inverse element)은 어떤 원소와 곱했을 때 항등원을 얻을 수 있는 원소`

`항등원(identity element)은 어떤 연산에 대해 그 연산의 결과를 변화시키지 않는 원소, 항등원은 모듈러 연산에서 `1. 

정수 a와 소수 p가 주어졌을때, **a의 역원 b는 a * b ≡ 1 (mod p)를 만족하는 정수 b이다.** 이때 a와 p가 서로소(1과 자신만 나누어짐)일때만 역원이 존재한다. 예를들어 2와 5는 서로소이므로, 2의 역원은 3이다. 즉, 2 * 3 ≡ 1 (mod 5)

그럼 위의 식에선 **a^p-2** 은 **a**의 역원을 의미한다. 예를들어 a가 2, p가 3일때, a^p-2 = 2, a^p-2 * a % 3 = 1

**a의 역원은 a^p-2가 된다. a^-1 또한 a의 역원이 될것이다.**

<br>

#### 페르마의 소정리(Fermat's little theorem)

`a와 p가 서로소이고, a가 p의 배수가 아니라면 a^(p-1)을 p로 나눈 나머지는 1과 같다. a^(p-1) ≡ 1 (mod p)`

위의 모듈러 연산의 역원과 페르마의 소정리에 따라 식을 증명해보자.

a와 p가 서로소이고, a가 p의 배수가 아닌 경우, 해당 a^p-2 ≡ a^-1 (mod p) 식의 양 변에 a^-1을 곱하면 

1. a^-1 * a^p-2 ≡ a^-1 * a^-1 (mod p)
2. a^-1+ (p-2) ≡ a^-2 (mod p)
3. 여기서, a^-2는 a^-1 * a^-1과 같으므로,
4. a^-1+ (p-2) ≡ a^-1 * a^-1 (mod p)

따라서  **a^(p-2) ≡ a^(p-1) * a^-1 ≡ 1 * a^-1 ≡ a^-1 (mod p)**이 성립한다.

그러므로 a와 p가 서로소이고, a가 p의 배수가 아닌 경우, **a^(p-2) ≡ a^(-1) (mod p) (a는 0이 아님)**이 성립된다.

<br>

### 이항계수의 조합 공식 변형

nCk은 N개의 원소 중에서 K개를 선택하는 경우의 수를 의미하며, 이를 구하는 방법 중 하나가 nCk = N! / (N-K)!K!이다.

nCk % p = **N! / (N-K)!K! % p**

여기서, 위에서 증명한 방법을 사용해보자. 우리는 역원(modular inverse)을 이용하여 분모의 역원을 곱해줄 수 있다. 즉, (N-K)!K!의 역원을 (N-K)!K!^(p-2)로 바꾸어 주면,

nCk % p = N! / (N-K)!K! % p  = **N!((N-K)!K!)^-1 % p**

 nCk % p = N! / (N-K)!K! % p  = N!((N-K)!K!)^-1 % p = **N!((N-K)!K!)^p-2 % p**

<br>

### 구현

N, K 를 입력받고, 1,000,000,007 으로 나눠야 하므로 변수에 저장을 해둔다.

팩토리얼을 구현한다. 1 부터 N까지 %p 연산을 하고 N! % p를 리턴한다.

팩토리얼은 이항계수의 조합 공식에서 팩토리얼 값을 %p연산이 적용된 값을 구할때 쓰인다.

``` python
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
p = 1000000007

# 팩토리얼
def factorial(N):
    n = 1
    # 나머지 연산을 적용한 팩토리얼 값 계산
    for i in range(2, N+1):
        n = (n * i) % p
    return n
```

<br>

분할정복을 이용해 거듭제곱 함수를 정의해준다.

거듭제곱 함수는 분모의 (N-K)!K!)^p-2 연산의 값을 구할때 사용된다.

``` python
# 거듭제곱
def square(N, K):
    if K == 0:
        return 1
    elif K == 1:
        return N
    
    temp = square(N, K//2)
    if K % 2:
        return temp * temp * N % p
    else:
        return temp * temp % p
```

<br>

위에서 도출한 N!((N-K)!K!)^p-2 % p 을 구현한다.

``` python
# N
numerator = factorial(N)
# (N-K) * K % p 
denominator = factorial(N-K) * factorial(K) % p
# N!((N-K)!K!)^p-2%p
print(numerator * square(denominator, p-2) % p)
```

<br>

### 전체코드

``` python
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
p = 1000000007

# 팩토리얼
def factorial(N):
    n = 1
    # 나머지 연산을 적용한 팩토리얼 값 계산
    for i in range(2, N+1):
        n = (n * i) % p
    return n

# 거듭제곱
def square(N, K):
    if K == 0:
        return 1
    elif K == 1:
        return N
    
    temp = square(N, K//2)
    if K % 2:
        return temp * temp * N % p
    else:
        return temp * temp % p
      
# N
numerator = factorial(N)
# (N-K) * K % p 
denominator = factorial(N-K) * factorial(K) % p
# N!((N-K)!K!)^p-2%p
print(numerator * square(denominator, p-2) % p)
```
