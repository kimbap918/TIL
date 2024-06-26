## 파이썬 알고리즘 수업 - 피보나치 수 1(백준 BOJ 24416)

<br>

동적 계획법

## 문제

오늘도 서준이는 동적 프로그래밍 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

오늘은 *n*의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여 *n*의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

피보나치 수 재귀호출 의사 코드는 다음과 같다.

```
fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
```

피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

```
fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
```

<br>

## 입력

첫째 줄에 *n*(5 ≤ *n* ≤ 40)이 주어진다.

<br>

## 출력

코드1 코드2 실행 횟수를 한 줄에 출력한다.

<br>

## 예제 입력 1

```
5
```

## 예제 출력 1

```
5 3
```

## 예제 입력 2

```
30
```

## 예제 출력 2

```
832040 28
```

<br>

## 📝 풀어보기

📌 문제에 함수 `fib` 와 `fibonacci`가 주어진다.

함수를 활용하여 파이썬에 맞게 바꾼 후 각각의 실행 횟수를 출력하면 된다.

피보나치 수는 **첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열**이다.

피보나치 수 문제는 재귀를 통해 풀 수 있는데, 재귀를 사용하면 n번 까지 자기자신을 호출해가며 계산을 하기 때문에 시간이 오래 걸린다. 그렇기 때문에 **미리 계산을 했다가 필요할 때 불러서 쓰는 방법인 동적 계획법**을 이용해야한다.

아래의 `fibonacci` 는 동적 계획법을 이용한 피보나치 수 구현 방법으로 주어진 `n` 의 범위가 *n*(5 ≤ *n* ≤ 40) 이므로 41개의 공간을 가진 리스트를 먼저 생성한 후 피보나치 수의 값을 미리 리스트 안에 저장해서 n이 입력됐을 때, 입력된 값에 해당하는 피보나치 수의 실행횟수를 출력한다.

``` python
# 첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.
def fib(n):
    # n이 1이나 2일때는 1을 리턴하고 아니면 fib(n - 1) + fib(n - 2)를 호출한다.
    # 자기 자신을 호출할때만 카운트를 올려줌
    global cnt1
    cnt1 += 1
    if n == 1 or n == 2:
        cnt1 -= 1
        return 1  # 코드1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    # 미리 계산했다가 필요할때 불러서 쓰기(동적 계획법)
    global cnt2
    f[1], f[2] = 1, 1 # 피보나치수에서 맨 처음과 두번째는 항상 1, 1
    for i in range(3, n+1): # 세번째부터 n까지 피보나치 수를 계산
        cnt2 += 1 # 이때부터 카운트
        f[i] = f[i-1]+f[i-2]
    return f[n]

cnt1, cnt2 = 0, 0
f = [0 for _ in range(41)]
n = int(input())
fib(n)
fibonacci(n)
print(cnt1+1, cnt2)
```

