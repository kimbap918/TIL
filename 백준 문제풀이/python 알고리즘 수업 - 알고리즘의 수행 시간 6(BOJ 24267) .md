## 파이썬 알고리즘 수업 - 알고리즘의 수행 시간 6(백준 BOJ 24267)

## 문제

오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

입력의 크기 *n*이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.

MenOfPassion 알고리즘은 다음과 같다.

```
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
```

## 입력

첫째 줄에 입력의 크기 *n*(1 ≤ *n* ≤ 500,000)이 주어진다.

<br>

## 출력

첫째 줄에 코드1 의 수행 횟수를 출력한다.

둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

<br>

## 예제 입력 1 

```
7
```

## 예제 출력 1 

```
35
3
```

코드1 이 35회 수행되고 알고리즘의 수행 시간이 *n3*에 비례한다.

<br>

## 📝풀어보기

``` python
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# 동작 확인
def MenOfPassion(A, n):
    sum = 0
    for i in range(1, n-1):
        A.append(1)
        for j in range(i+1, n):
            A.append(1)
            for k in range(j+1, n+1):
                A.append(1)

    for i in range(1, n-1):
        print("i : "+str(i))
        for j in range(i+1, n):
            print("j : "+str(j))
            for k in range(j+1, n+1):
                print("k : "+str(k))

                sum += A[i] * A[j] * A[k]
    return sum

A = []
n = int(input())
print(MenOfPassion(A, n))

# 제출코드
print(int((n-2)*(n-1)*n/6))
print(3)
```

