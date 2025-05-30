

## 파이썬 N과 M(5)(BOJ 15653)

<br>

## 문제

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열

<br>

## 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

<br>

## 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제 입력 1 

```
3 1
4 5 2
```

## 예제 출력 1 

```
2
4
5
```

## 예제 입력 2 

```
4 2
9 8 7 1
```

## 예제 출력 2 

```
1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8
```

## 예제 입력 3 

```
4 4
1231 1232 1233 1234
```

## 예제 출력 3 

```
1231 1232 1233 1234
1231 1232 1234 1233
1231 1233 1232 1234
1231 1233 1234 1232
1231 1234 1232 1233
1231 1234 1233 1232
1232 1231 1233 1234
1232 1231 1234 1233
1232 1233 1231 1234
1232 1233 1234 1231
1232 1234 1231 1233
1232 1234 1233 1231
1233 1231 1232 1234
1233 1231 1234 1232
1233 1232 1231 1234
1233 1232 1234 1231
1233 1234 1231 1232
1233 1234 1232 1231
1234 1231 1232 1233
1234 1231 1233 1232
1234 1232 1231 1233
1234 1232 1233 1231
1234 1233 1231 1232
1234 1233 1232 1231
```

<br>

## 📝 풀어보기

백트래킹을 이용한 문제

<br>

N개의 자연수, 길이가 M인 수열을 입력받는다.

N개의 수를 담아서 arr에 저장한다. 그리고 오름차순으로 정렬한다.

방문을 확인하기 위해 [False]를 N개만큼 저장해둔다. 

ans는 정답이 되는 수열을 담기 위해 빈 리스트를 저장해둔다. 

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
ans = []

```

<br>

backtraking 함수를 정의한다.

깊이(depth)가 M과 같아지면 ans의 값들을 출력한다.

N만큼 반복하면서 방문하지 않은 visited 요소가 있으면 방문처리를 하고 ans에 현재 순회중인 arr의 요소값을 ans에 추가해준다.

그리고 depth를 1증가시켜준다.

여기서 예제2, 예제3 같이 사용한 숫자들을 다시 사용해야하므로 백트래킹을 이용한다. 

사용한 ans값을 꺼내고, 해당 요소의 방문처리를  False로 변경한다.

```python
def backtraking(depth, N, M):
    if depth == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[i])
            backtraking(depth+1, N, M)
            # 백트래킹
            ans.pop()
            visited[i] = False


backtraking(0, N, M)
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
ans = []

def backtraking(depth, N, M):
    if depth == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[i])
            backtraking(depth+1, N, M)
            # 백트래킹
            ans.pop()
            visited[i] = False


backtraking(0, N, M)
```

