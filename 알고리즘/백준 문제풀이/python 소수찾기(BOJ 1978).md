## 파이썬 소수 찾기(백준 BOJ 1978)

<br>

## 문제

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

<br>

## 입력

첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

<br>

## 출력

주어진 수들 중 소수의 개수를 출력한다.

<br>

## 예제 입력 1

```
4
1 3 5 7
```

## 예제 출력 1

```
3
```

<br>

## 📝 풀어보기

📌 테스트케이스 `T`, 입력할 숫자 `A`, 소수를 담을 리스트 `B`, 소수를 계산할 기준인 최대값 `A`, 소수를 카운트할 `cnt` 를 선언한다. 

``` python
T = int(input())
A = list(map(int, input().split()))
B = []
max = 0
cnt = 0
```

<br>

📌 입력한 리스트 A의 길이만큼 반복하면서 A에서 최대값을 구한다

``` python
for i in range(len(A)): # 가장 큰 수 구하기
    if max < A[i]:
        max = A[i]
```

<br>

📌 소수를 구할때 에라토스테네스의 체 방식을 사용했다. 2부터 max+1의 범위까지 중에 소수가 있으면 판별해서 모두 리스트 B에  추가한다.

``` python
# 소수 구하기/에라토스테네스의 체
for n in range(2, max+1): # 2부터 max+1까지 
    check = True          
    for i in range(2, int(n**0.5)+1): # 2부터 n의 제곱근까지만 검사
        if n%i == 0:                  # n%i가 소수가 아닌 경우 
            check = False
    if check: # 소수인경우 
        B.append(n)
```

<br>

📌 최대 max값까지의 범위 내에서 소수가 담긴 리스트 B를 이제 입력한 A와 비교한다. A 안에 B의 값들이 있으면 카운트를 증가시키고 출력한다.

``` python
for k in B: # 리스트 B와 A 비교
    for h in range(len(A)):
        if A[h] == k: # k의 값(소수)이 리스트 A에 있는 값과 같다면
            cnt += 1 # 카운트 증가
print(cnt)
```

<br>

#### 전체코드

``` python
T = int(input())
A = list(map(int, input().split()))
B = []
max = 0
cnt = 0

for i in range(len(A)): # 가장 큰 수 구하기
    if max < A[i]:
        max = A[i]

# 소수 구하기/에라토스테네스의 체
for n in range(2, max+1): # 2부터 max+1까지 
    check = True          
    for i in range(2, int(n**0.5)+1): # 2부터 n의 제곱근까지만 검사
        if n%i == 0:                  # n%i가 소수가 아닌 경우 
            check = False
    if check: # 소수인경우 
        B.append(n)

for k in B: # 리스트 B와 A 비교
    for h in range(len(A)):
        if A[h] == k: # k의 값(소수)이 리스트 A에 있는 값과 같다면
            cnt += 1 # 카운트 증가
print(cnt)
```

