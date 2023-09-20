## 파이썬 나무 자르기(BOJ 2805)

<br>

## 문제

상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

<br>

## 출력

적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

<br>

## 예제 입력 1 

```
4 7
20 15 10 17
```

## 예제 출력 1

```
15
```

## 예제 입력 2

```
5 20
4 42 40 26 46
```

## 예제 출력 2

```
36
```

<br>

## 📝 풀어보기

나무 절단기의 높이를 움직여서 가져갈 나무 길이를 맞춰보기

![binary_search](../../binary_search.gif)

<br>

랜선 자르기(BOJ 1654)와 유사한 문제다.

나무의 수 N과 가져가려고 하는 나무 길이 M을 입력받고

N만큼 나무의 높이를 각각 저장한다.

시작지점은 1, 입력받은 나무 중 최대 높이를 끝지점으로 저장한다.

``` python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
logs = list(map(int, input().split()))
start, end = 1, max(logs)
```

<br>

이분 탐색 함수를 만든다.

중간지점을 정하고 저장한다.

잘라가야할 나무의 총합을 저장하기 위한 변수를 만들어두고, 나무의 높이가 입력된 리스트 요소를 순회하면서 중간값보다 i가 크거나 같을때 i-mid 값을 총합에 누적한다.

합산된 나무의 길이가 M을 넘거나 같으면 시작지점을 mid+1로 갱신하고, 반대의 경우에는 끝지점을 mid-1로 갱신한 뒤에 조건이 만족할때 까지 반복한다.  

```python
def binary_search(start, end):
    while start <= end:
        mid = (start+end) // 2
        log = 0
        for i in logs:
            if i >= mid:
                log += (i - mid)
        if log >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(start, end))
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
logs = list(map(int, input().split()))
start, end = 1, max(logs)

def binary_search(start, end):
    while start <= end:
        mid = (start+end) // 2
        log = 0
        for i in logs:
            if i >= mid:
                log += (i - mid)
        if log >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(start, end))
```



