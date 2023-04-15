## 파이썬 가장 긴 증가하는 부분 수열 4(BOJ 14002)

<br>

## 문제

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {**10**, **20**, 10, **30**, 20, **50**} 이고, 길이는 4이다.

<br>

## 입력

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

<br>

## 출력

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

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

이 문제는 이전에 풀었던 **가장 긴 증가하는 부분 수열(BOJ 11053)**과 굉장히 유사하다.

조금 다른점은 출력에 가장 긴 증가하는  부분 수열을 출력하는 것이다.

<br>

가장 긴 증가하는 부분 수열의 길이를 구하는 코드는 이전과 다를게 없다.

``` python
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(N+1)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
```

<br>

dp의 최대값을 ans1변수에 저장해둔다.

결과값을  담을 리스트 하나를 생성하고 N의 역순으로 순회한다.

끝에서 부터, `dp[i]` 값과 ans1(dp의 최대값)이 일치하면, 해당 `A[i]` 값을 리스트에 추가시키고 ans1을 1 감소시킨다.

res 리스트에는 값들이 역순으로 들어가 있기때문에, 다시 res의 순서를 뒤집어주고 res의 길이와 값을 출력한다.

``` python
ans1 = max(dp)
res = []
for i in range(N-1, -1, -1):
    if dp[i] == ans1:
        res.append(A[i])
        ans1 -= 1
res.reverse()
print(len(res))
for i in res:
    print(i, end=' ')
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(N+1)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

ans1 = max(dp)
res = []
for i in range(N-1, -1, -1):
    if dp[i] == ans1:
        res.append(A[i])
        ans1 -= 1
res.reverse()
print(len(res))
for i in res:
    print(i, end=' ')
```

