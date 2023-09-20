## 파이썬 가장 긴 증가하는 부분 수열 2(BOJ 12015)

<br>

## 문제

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {**10**, **20**, 10, **30**, 20, **50**} 이고, 길이는 4이다.

<br>

## 입력

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

<br>

## 출력

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

<br>

## 예제 입력 1

```
6
10 20 10 30 20 50
```

## 예제 출력 1 

```
4
```

<br>

## 📝 풀어보기

<br>

이 문제의 이전에 풀었던 **가장 긴 증가하는 부분 수열(BOJ 11053)**의 코드를 살펴보자

``` python
N = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(N)]

for i in range(N):
  	for j in range(i):
      	if A[i] > A[j] and dp[i] > dp[j]:
          	dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
```

이전에 나는 수열의 길이를 담은 dp 리스트를 만들어서 N만큼의 반복문을 돌리고 다시 i만큼 반복하면서 A리스트를 순회했고, `A[i]` 값과 i 범위 안에서 `A[j]` 값을 비교해가면서 증가하는 수열이 있으면 `dp[i]` 값을 1씩 증가시켰고, 마지막에 dp의 최대값을 출력시키는 방식으로 가장 긴 증가하는 부분 수열을 구했다.

하지만 반복문이 2중으로 사용되는 만큼, N의 범위가 커지면 시간초과에 걸리기 쉽다. 

가장 긴 증가하는 부분 수열2 에서는 1,000이던 N의 범위가 1,000,000으로 증가해서 위의 방법으로는 구할 수 없기때문에 이분 탐색으로 구현했다.

<br>

처음에 문제의 예제 입출력만 보고 착각했던 부분이 있다.

#### 입력

``` 
6
10 20 10 30 20 50
```

#### 출력

```
4
```

여기서 증가하는 부분 수열은 어떻게 되는가?

[10, 20, 30, 50] 일것이다.

그렇다면 아래는 어떻게 될까?

#### 입력

``` 
6
10 20 15 18 30 40
```

출력은 [10, 20, 30, 40] 이 될것이라 생각했지만 [10, 15, 18, 30, 40]이 된다.

#### 출력

```
10 15 18 30 40
```

<br>

이 문제에서 수열이 채워지는 순서는 다음과 같다.

``` python
10
10 20
10 15 18
10 15 18 30 
10 15 18 30 40
```

처음에 이 문제에서 10 20 이 나왔다면 다음의 수가 20보다 작은 15 18은 무시되고 30 40을 채운다고 생각했다.

수열의 정의를 보면 

> *수열*(數列) 또는 열(列, sequence)은 수 또는 다른 대상*의* 순서 있는 나열이다. 나열 순서를 생각해야 하고 중복이 허용된다.  

수열이란 일정한 규칙에 따라서 숫자들이 나열되어야 한다. 하지만 숫자 [10, 15, 18, 30, 40]은 수열이 될 수 없다. 규칙성이 없기 때문이다. 이 말의 이해를 돕기 위해 chat GPT에게 물어봤다.

<img width="827" alt="스크린샷 2023-04-14 오후 4 11 40" src="https://user-images.githubusercontent.com/75712723/231970662-b5865949-d2e8-46c2-a930-b6a43280ce75.png">

<br>

그렇다면, 여기서는 왜 10 15 18 30 40 즉, 5가 정답이 될까?

그 이유는 가장 긴 증가하는 부분 수열 자체를 구하는것이 아니라 가장 긴 길이를 구하기 위해서 수열의 형태만 사용했기 때문이다.

이 점을 참고해서 코드를 보자.

<br>

삽입되는 수의 개수 N, 수가 담긴 리스트 A를 입력받고 증가하는 부분 수열을 담을 리스트 dp를 생성한다.

``` python
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = []
```

<br>

이분 탐색 함수를 구현한다.

입력된 모든 수를 파악하기 위해 N만큼 반복하면서, 시작점과 끝점을 저장해둔다. 끝점을 len(dp)-1로 한 이유는 len(dp)로 저장할 시

dp 리스트의 길이를 초과해서 탐색하기 때문에 index out of range가 걸린다.

중간지점(mid)를 생성하고 `dp[mid]`가 `A[i]` 보다 값이 작으면 시작점을 mid + 1로 하고 반대의 경우 끝지점을 mid -1 로 해서 while문이 끝날 때 까지 재탐색한다.

dp의 길이보다 시작점의 값이 크거나 같으면, dp에 `A[i]`값을 추가한다. 그외엔 `dp[start]` 값을 `A[i]`로 갱신시켜주고 반복이 끝나면 dp의 길이를 리턴한다. 

``` python
def binary_search(arr):
    # N만큼 반복
    for i in range(N):
        # 시작지점, 끝지점 지정
        start, end = 0, len(dp)-1
        while start <= end:
            mid = (start+end) // 2
            if dp[mid] < arr[i]:
                start = mid + 1
            else:
                end = mid - 1
        # dp 의 길이보다 시작점이 길면
        if start >= len(dp):
            # A[i] 추가
            dp.append(arr[i])
        else:
            # dp[0] = A[0]
            dp[start] = arr[i]

    return len(dp)
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = []

def binary_search(arr):
    # N만큼 반복
    for i in range(N):
        # 시작지점, 끝지점 지정
        start, end = 0, len(dp)-1
        while start <= end:
            mid = (start+end) // 2
            if dp[mid] < arr[i]:
                start = mid + 1
            else:
                end = mid - 1
        # dp 의 길이보다 시작점이 길면
        if start >= len(dp):
            # A[i] 추가
            dp.append(arr[i])
        else:
            # dp[0] = A[0]
            dp[start] = arr[i]

    return len(dp)

print(binary_search(A))
```

