

## 파이썬 오큰수(BOJ 17298)

<br>

## 문제

크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

<br>

## 입력

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

<br>

## 출력

총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

<br>

## 예제 입력 1 

```
4
3 5 2 7
```

## 예제 출력 1 

```
5 7 7 -1
```

## 예제 입력 2 

```
4
9 5 4 8
```

## 예제 출력 2 

```
-1 8 8 -1
```

<br>

## 📝 풀어보기

수열 A의 크기 N을 입력받는다.

수열 A의 값을 입력받고 오큰수를 담을 리스트 NGE에 -1을 N만큼 저장해둔다.

-1을 저장해 둔 이유는 예제의 출력에서 오큰수가 없을 경우에는 -1로 출력되게 하는 조건이 있기 때문이다.

stack 리스트를 생성해둔다. stack에는 수열 A의 순서에 따른 값과 인덱스를 담는다.

``` python
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())) # 3 5 2 7
NGE = [-1] * N
stack = []
```

<br>

N의 범위를 순회하면서, stack에 값이 있으면 stack이 비거나 stack의 맨 마지에 저장된 수열 A의 요소가 순회하고 있는 현재 A[i]보다 커질때까지 반복하며 num, idx 에 stack에서 꺼낸 값을 저장하고, 오큰수 NGE에 stack에서 꺼낸 idx 위치에 현재 순회하는 A[i]값을 저장한다.

stack이 비어있다면 현재 순회하는 A[i]값과, 인덱스 i를 넣어주고 수열 A를 모두 순회할때까지 반복한다.

```python
# 오른쪽에 있으면서 Aj보다 큰 수 중에서 가장 왼쪽에 있는 수
for i in range(N):
    while stack and stack[-1][0] < A[i]:
        # arr값과 인덱스를 꺼낸다
        num, idx = stack.pop()
        NGE[idx] = A[i]
    stack.append([A[i], i])
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())) # 3 5 2 7
NGE = [-1] * N
stack = []

# 오른쪽에 있으면서 Aj보다 큰 수 중에서 가장 왼쪽에 있는 수
for i in range(N):
    while stack and stack[-1][0] < A[i]:
        # arr값과 인덱스를 꺼낸다
        num, idx = stack.pop()
        NGE[idx] = A[i]
    stack.append([A[i], i])

print(*NGE)
```

