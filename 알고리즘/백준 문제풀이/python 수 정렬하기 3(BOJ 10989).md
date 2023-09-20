## 파이썬 수 정렬하기 3(백준 BOJ 10989) 

<br>

## 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

<br>

## 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

<br>

## 예제 입력 1 

```
10
5
2
3
1
4
2
3
5
1
7
```

## 예제 출력 1

```
1
1
2
2
3
3
4
5
5
7
```

<br>

## 📝 풀어보기

📌 첫째줄에 수의 개수가 아주 많다. `N(1 ≤ N ≤ 10,000,000)`

시간초과를 받지않기 위해 readline을 사용했다. 수의 범위는 1부터 10000까지이기 때문에 num_list에 [0]인 리스트를 미리 10001개 생성한다.

``` python
import sys
input = sys.stdin.readline
n = int(input())
num_list = [0] * 10001 # 1부터 10000까지 값, 인덱스는 0부터 세기때문에 계산하기 편하게 10001
```

<br>

📌 N만큼 반복하면서 입력된 값의 인덱스에 1을 추가한다.

10001번 반복하면서 num_list[i]에 0보다 큰 값을 갖는 인덱스를 찾아서 출력해낸다.

``` python
for _ in range(n):
    num_list[int(input())] += 1 # 입력된 값의 인덱스에 +1

for i in range(10001):
    if num_list[i] != 0: # 0보다 큰 요소를 갖는 인덱스를 찾아서 출력
        for j in range(num_list[i]):
            print(i)
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline
n = int(input())
num_list = [0] * 10001 # 1부터 10000까지 값, 인덱스는 0부터 세기때문에 계산하기 편하게 10001

for _ in range(n):
    num_list[int(input())] += 1 # 입력된 값의 인덱스에 +1

for i in range(10001):
    if num_list[i] != 0: # 0보다 큰 요소를 갖는 인덱스를 찾아서 출력
        for j in range(num_list[i]):
            print(i)
```

