## 파이썬 K번째 수(BOJ 1300)

<br>

## 문제

세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.

<br>

## 입력

첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(109, N2)보다 작거나 같은 자연수이다.

<br>

## 출력

B[k]를 출력한다.

<br>

## 예제 입력 1

```
3
7
```

## 예제 출력 1

```
6
```

<br>

## 📝 풀어보기

<br>

문제를 풀기 전에 이 문제의 배열을 먼저 나열해보자.

3x3

[1, 1] [1, 2] [1, 3]

[2, 1] [2, 2] [2, 3]

[3, 1] [3, 2] [3, 3]

**B = [1, 2, 3, 2, 4, 6, 3, 6, 9]**

B[7] = 6

이 문제는 단순히 보면

``` python
import sys
input = sys.stdin.readline

N, K = int(input()), int(input())
B = []

for i in range(1, N+1):
  for j in range(1, N+1):
    B.append(i*j)
    
print(B[K])
    
```

와 같은 방식으로 풀면 풀릴것같지만, 수의 범위가 크다. 단순히 반복문을 두 개 돌려서 곱한 값을 저장한 후 B의 K번째 인덱스를 찾는다면 N의 크기가 100,000 정도만 되어도 시간초과가 걸릴것이다.

<br>

이 문제는 의외로 이분 탐색으로 해결이 가능하다.

이분 탐색으로 어떤 수보다 작은 자연수의 곱(ixj)이 몇 개인지 알아내보자.

만약 어떤 수 보다 작은숫자가 몇개인지 알 수 있으면 어떤 수가 몇번째 숫자인지도 알수 있다.

<br>

예를들어 N이 3일때, 3x3배열에서 7보다 작거나 같은 수를 구하는 법을 찾아보자.

1x1 ~ 1x3 = 1, 2, 3 = 3개 (배열이 NxN이므로 최대 크기인 N을 넘을 수 없음)

2x1 ~ 2x3 = 2, 4, 6 = 3개

3x1 ~ 3x2 = 3, 6 = 2개

**B = [1, 2, 3, 2, 4, 6, 3, 6]**

나열해 보면 맨 처음에 본 배열과 같다는걸 알 수 있다.

<br>

위의 답은 아래와 같이 나타낼 수 있다.

7 // 1 = 3 (배열이 NxN이므로 최대 크기인 N을 넘을 수 없음)

7 // 2 = 3

7 // 3 = 2

즉, 식으로 표현해보면

``` python
N, K = int(input()), int(input())
start, end = 1, K

temp = 0
mid = (start+end) // 2
for i in range(1, N+1):
  	temp += min(mid//i, N) # 최대 N을 넘을 수 없다
```

이 될것이다.

<br>

위와 같은 방법으로 해당 숫자(mid) 보다 작거나 같은 숫자를 전부 찾아서 mid가 몇번째에 위치한 숫자인지 알아내면 된다.

#### 전체코드

``` python
import sys
input = sys.stdin.readline

N, K = int(input()), int(input())
start, end = 1, K

def binary_search(start, end):
    res = 0
    while start <= end:
        temp = 0
        mid = (start+end) // 2
        for i in range(1, N+1):
            temp += min(mid//i, N)
        if temp >= K:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res


print(binary_search(start, end))
```

