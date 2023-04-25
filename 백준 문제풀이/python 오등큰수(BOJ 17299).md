

## 파이썬 오등큰수(BOJ 17299)

<br>

## 문제

크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.

Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오등큰수는 -1이다.

예를 들어, A = [1, 1, 2, 3, 4, 2, 1]인 경우 F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1이다. A1의 오른쪽에 있으면서 등장한 횟수가 3보다 큰 수는 없기 때문에, NGF(1) = -1이다. A3의 경우에는 A7이 오른쪽에 있으면서 F(A3=2) < F(A7=1) 이기 때문에, NGF(3) = 1이다. NGF(4) = 2, NGF(5) = 2, NGF(6) = 1 이다.

<br>

## 입력

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

<br>

## 출력

총 N개의 수 NGF(1), NGF(2), ..., NGF(N)을 공백으로 구분해 출력한다.

<br>

## 예제 입력 1

```
7
1 1 2 3 4 2 1
```

## 예제 출력 1

```
-1 -1 1 2 2 1 -1
```

<br>

## 📝 풀어보기

앞서 풀었던 오큰수(BOJ 17298)과 문제가 매우 유사하다.

처음에는 count() 함수로 문제를 풀려고 했으나 시간초과가 발생해서 알아보니까 collections 모델에 Counter 라는 클래스가 있어서 활용했다.

**collections 모듈의 Counter 클래스**는 **컨테이너안의 데이터를 편리하고 빠르게 개수를 세도록 지원하는 계수기 도구이다.** 반환 형태는 Dictionary 이기 때문에 빠르게 개수를 셀 수 있다.

예시를 보자.

``` python
from collections import Counter
arr = ["참치", "꽁치", "멸치", "멸치", "참치", "가물치", "쥐치", "참치", "꽁치", "멸치", "멸치"]
arr_cnt = Counter(arr)

print(arr_cnt)

>> Counter({'멸치': 4, '참치': 3, '꽁치': 2, '가물치': 1, '쥐치': 1})
```

이것을 이용하여 숫자를 담은 수열 A의 요소 개수를 파악해서 문제를 풀면 된다.

<br>

#### 전체코드

``` python
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A_cnt = Counter(A)
NGF = [-1] * N
stack = []

for i in range(N):
    while stack and stack[-1][0] < A_cnt[A[i]]:
        num, idx = stack.pop()
        NGF[idx] = A[i]
    stack.append([A_cnt[A[i]], i])

print(*NGF)
```

