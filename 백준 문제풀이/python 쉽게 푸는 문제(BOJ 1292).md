## 파이썬 쉽게 푸는 문제(백준 BOJ 1292)

<br>

## 문제

동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

<br>

## 입력

첫째 줄에 구간의 시작과 끝을 나타내는 정수 A, B(1 ≤ A ≤ B ≤ 1,000)가 주어진다. 즉, 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다.

<br>

## 출력

첫 줄에 구간에 속하는 숫자의 합을 출력한다.

<br>

## 예제 입력 1

```
3 7
```

## 예제 출력 1

```
15
```

<br>

## 📝 풀어보기

이 문제를 나는 for 문으로 풀었는데 풀고보니 좀 무식하게 푼것같다.

#### for를 이용한 방법

📌 수열을 담을 리스트 `row`를 만들고 List Comprehension으로 46까지 1부터 숫자만큼 개수가 증가하는 수열을 생성한다. range가 46인 이유는 A와 B의 범위제한이 수열의 1000번째 인덱스까지인데, 46까지 나열하면 1000이 나오기 때문이다.

 ``` python
 row = []
 [row.append(i) for i in range(46) for j in range(i)]        
 ```

<br>

📌 A, B를 입력받아 시작과 끝의 값을 받고 인덱스 슬라이싱으로 가져온 값을 합산해서 출력한다.

``` python
A, B = map(int, input().split()) # 입력
print(sum(row[A-1:B])) # 출력
```

<br>

#### while을 이용한 방법

📌 수열을 입력받을 리스트 `row` 시작과 끝 값을 받을 `A, B` 수열의 시작값 1을 만든다.

``` python
# 방법 2
row = []
A, B = map(int, input().split())
N = 1
```

<br>

📌 row 리스트의 길이값이 B보다 커질때까지 반복하면서 N의 값을 리스트에 추가하고 N을 누적시킨다. 반복이 종료되면 인덱스 슬라이싱으로 가져온 값을 합산해서 출력한다.

``` python
# 수열이 B보다 커질때까지
while len(row) < B:
    # N의 길이동안
    for _ in range(N):
        # N_list에 추가
        row.append(N)
    # N에 1 누적    
    N += 1

print(sum(N_list[A-1:B])) 
```

<br>

#### 전체코드

``` python
# 방법 1
row = []
[row.append(i) for i in range(46) for j in range(i)]        
A, B = map(int, input().split()) # 입력
print(sum(row[A-1:B])) # 출력


row = []
for i in range(0, 46):
    for j in range(i):
        row.append(i)

# 방법 2
row = []
A, B = map(int, input().split())
N = 1

# 수열이 B보다 커질때까지
while len(row) < B:
    # N의 길이동안
    for _ in range(N):
        # N_list에 추가
        row.append(N)
    # N에 1 누적    
    N += 1

print(sum(N_list[A-1:B])) 
```

