## 파이썬 가장 긴 증가하는 부분 수열 5(BOJ 14003)

<br>

## 문제

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {**10**, **20**, 10, **30**, 20, **50**} 이고, 길이는 4이다.

<br>

## 입력

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (-1,000,000,000 ≤ Ai ≤ 1,000,000,000)

<br>

## 출력

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력한다.

<br>

## 예제 입력 1 

```
6
10 20 10 30 20 50
```

## 예제 출력 1

```
4
10 20 30 50
```

<br>

## 📝 풀어보기

<br>

이 문제는 **가장 긴 증가하는 부분 수열4(BOJ 14002)**와 같이 부분 수열을 출력하면서, N의 범위가 **가장 긴 증가하는 부분 수열 2(BOJ 12015)** 처럼 1 ≤ N ≤ 1,000,000에 해당하기 때문에 이분탐색으로 풀어야 한다.

<br>

이분 탐색을 먼저 구현했다. 인자는 시작점, 끝점, 입력받을 수열 리스트 A의 원소다.

``` python
import sys
input = sys.stdin.readline

def binary_search(start, end, arr_num):
    while start < end:
        mid = (start+end) // 2
        if lis[mid] < arr_num:
            start = mid + 1
        else:
            end = mid
    return end
```

<br>

삽입할 숫자의 개수 N, 삽입하는 숫자 리스트 A를 입력받는다.

lis는 증가하는 부분 수열을 담아, `A[i]`와 비교하기 위해 생성했다. 초기값은 A의 첫번째 원소를 넣었다.

Idx_val은  **가장 긴 증가하는 부분 수열4(BOJ 14002)**에서 구현했던 dp와 비슷한 역할을 한다. 여기에 실제 저장되는 값까지 더해 lis의 길이와, 해당 `A[i]`의 값을 같이 저장한다. 여기에도 각 원소의 1번째 인덱스에 초기값으로 `A의 첫번째 원소를 저장해둔다.

A[0]값은 이미 삽입되어있기 때문에 1부터 N까지 순회한다. `idx_val[i][1]`에 `A[i]`를 저장하고 lis의 마지막 요소가 A[i]보다 작다면, 다음에 들어올 값이 크기 때문에 `idx_val[i][0]`에 lis의 길이를 저장하고, lis에는 해당하는 A원소의 값을 저장한다.

lis의 마지막 요소가 A[i]보다 크다면? A[i]가 들어갈 자리를 찾아야한다. 여기서 들어갈 인덱스를 이분탐색한다.

이분탐색으로 값을 찾아 `idx_val[i][0]`에 해당 값을 저장한다.  `lis[idx]`에 A의 해당 원소의 값을 저장한다.

``` python
N = int(input()) # 삽입할 숫자의 개수
A = list(map(int, input().split())) # 숫자의 리스트
lis = [A[0], ] # 증가하는 부분 수열을 담아 비교
idx_val = [[0,0] for _ in range(N)] # 증가하는 부분 수와 인덱스를 담는 리스트
idx_val[0][1] = A[0] # 각 원소 2번째칸에 A[0] 저장

for i in range(1, N):
    idx_val[i][1] = A[i] # 순회하는 원소의 2번째 칸에 증가하는 부분 수 저장
    # A[i]가 lis의 마지막보다 클 경우
    if lis[-1] < A[i]: # lis의 마지막과 A[i]원소 비교
        idx_val[i][0] = len(lis) # 길이 저장
        lis.append(A[i]) # A[i] lis에 저장
    else: # A[i]가 lis의 마지막보다 작을 경우
        idx = binary_search(0, len(lis)-1, A[i])
        idx_val[i][0] = idx
        lis[idx] = A[i]
```

<br>

반복을 종료하고 비교와 출력을 위해 idx를 lis의 길이 -1로  갱신해준다.

N의 역순으로 순회하면서 idx와 저장해둔 인덱스를 비교한다. 일치하면 해당하는 값을 res에 담고 인덱스를 1씩 감소시킨다.

인덱스가 -1이 되면 종료한다.

마지막으로 결과를 담아둔 res의 길이와 값을 출력한다.

``` python
idx = len(lis)-1
res = []
for i in range(N-1, -1, -1):
    if idx == -1:
        break
    if idx == idx_val[i][0]:
        res.append(idx_val[i][1])
        idx -= 1

print(len(res))
print(*res[::-1])
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

def binary_search(start, end, arr_num):
    while start < end:
        mid = (start+end) // 2
        if lis[mid] < arr_num:
            start = mid + 1
        else:
            end = mid
    return end

N = int(input()) # 삽입할 숫자의 개수
A = list(map(int, input().split())) # 숫자의 리스트
lis = [A[0], ] # 증가하는 부분 수열의 개수를 담을 리스트
idx_val = [[0,0] for _ in range(N)] # 증가하는 부분 수와 인덱스를 담는 리스트
idx_val[0][1] = A[0] # 각 원소 2번째칸에 A[0] 저장

for i in range(1, N):
    idx_val[i][1] = A[i] # 순회하는 원소의 2번째 칸에 증가하는 부분 수 저장
    # A[i]가 lis의 마지막보다 클 경우
    if lis[-1] < A[i]: # lis의 마지막과 A[i]원소 비교
        idx_val[i][0] = len(lis) # 길이 저장
        lis.append(A[i]) # A[i] lis에 저장
    else: # A[i]가 lis의 마지막보다 작을 경우
        idx = binary_search(0, len(lis)-1, A[i])
        idx_val[i][0] = idx
        lis[idx] = A[i]

idx = len(lis)-1
res = []
for i in range(N-1, -1, -1):
    if idx == -1:
        break
    if idx == idx_val[i][0]:
        res.append(idx_val[i][1])
        idx -= 1

print(len(res))
print(*res[::-1])

```

