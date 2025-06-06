## 파이썬 검문(백준 BOJ 2981)

<br>

## 문제

트럭을 타고 이동하던 상근이는 경찰의 검문을 받게 되었다. 경찰은 상근이가 운반하던 화물을 하나하나 모두 확인할 것이기 때문에, 검문하는데 엄청나게 오랜 시간이 걸린다.

상근이는 시간을 때우기 위해서 수학 게임을 하기로 했다.

먼저 근처에 보이는 숫자 N개를 종이에 적는다. 그 다음, 종이에 적은 수를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾으려고 한다. M은 1보다 커야 한다.

N개의 수가 주어졌을 때, 가능한 M을 모두 찾는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 종이에 적은 수의 개수 N이 주어진다. (2 ≤ N ≤ 100)

다음 줄부터 N개 줄에는 종이에 적은 수가 하나씩 주어진다. 이 수는 모두 1보다 크거나 같고, 1,000,000,000보다 작거나 같은 자연수이다. 같은 수가 두 번 이상 주어지지 않는다.

항상 M이 하나 이상 존재하는 경우만 입력으로 주어진다.

<br>

## 출력

첫째 줄에 가능한 M을 공백으로 구분하여 모두 출력한다. 이때, M은 증가하는 순서이어야 한다.

<br>

## 예제 입력 1

```
3
6
34
38
```

## 예제 출력 1

```
2 4
```

## 예제 입력 2

```
5
5
17
23
14
83
```

## 예제 출력 2

```
3
```

<br>

## 📝 풀어보기

📌 시간초과 방지를 위해 readline을 사용한다.

종이에 적은 개수 N을 입력받고 종이에 적은 수를 arr에 추가한다.

최대공약수를 담을 gcds에 arr[1]-arr[0] 의 절대값을 저장해둔다. 

``` python
import sys
input = sys.stdin.readline

# 3
# 6
# 34
# 38
N = int(input())
arr = []

for i in range(N):
    n = int(input())
    arr.append(n) # [6, 34, 28]

gcds = [abs(arr[1]-arr[0])] # 34 - 6 = 28
```

<br>

📌 gcd 함수를 생성해서 b가 0이 될때 a를 리턴하고 그외엔 유클리드 호제법으로 b, a%b를 리턴한다. 

``` python
def gcd(a,b): # 4, 28
    if b == 0:
        return a
    # print(gcd(b, a%b))
    return gcd(b, a%b) # 28, 6 / 6, 4 / 4, 2 / 2, 0 => 2 return
```

<br>

📌 2부터 arr의 길이까지 반복하면서 arr[j] - arr[j-1], gcds[0]를 유클리드 호제법으로 최대공약수를 구한 값을 gcds에 추가한다.

gcds를 오름차순 정렬하고 답을 넣을 ans 리스트를 생성한다.

gcds 첫번째 요소의 제곱근까지만 탐색하면서 gcds[0] % k 가 0이면 ans에 k와 gcds[0] // k 값을 추가한다.

ans를 중복제거하고 다시정렬한 후 ans의 1번째 인덱스부터 차례로 출력한다. 

``` python
for j in range(2, len(arr)):
    gcds.append(gcd(abs(arr[j] - arr[j - 1]), gcds[0])) # (arr[2] - arr[1])(28-34= 6), 28
gcds.sort() # 오름차순 정렬
ans = []
for k in range(1, int(gcds[0] ** 0.5) + 1): # gcds 첫번째 요소의 제곱근까지만 탐색
    if gcds[0] % k == 0: # 2 % 1 = 0
        ans.append(k) # 1
        ans.append(gcds[0] // k) # 2 // k = 2
ans = list(set(ans)) # 2
ans.sort()

for l in ans[1:]: # m이 1보다 커야하므로
    print(l, end=" ")
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

# 3
# 6
# 34
# 38
N = int(input())
arr = []

for i in range(N):
    n = int(input())
    arr.append(n) # [6, 34, 28]

gcds = [abs(arr[1]-arr[0])] # 34 - 6 = 28

def gcd(a,b): # 4, 28
    if b == 0:
        return a
    # print(gcd(b, a%b))
    return gcd(b, a%b) # 28, 6 / 6, 4 / 4, 2 / 2, 0 => 2 return

for j in range(2, len(arr)):
    gcds.append(gcd(abs(arr[j] - arr[j - 1]), gcds[0])) # (arr[2] - arr[1])(28-34= 6), 28
gcds.sort() # 오름차순 정렬
ans = []
for k in range(1, int(gcds[0] ** 0.5) + 1): # gcds 첫번째 요소의 제곱근까지만 탐색
    if gcds[0] % k == 0: # 2 % 1 = 0
        ans.append(k) # 1
        ans.append(gcds[0] // k) # 2 // k = 2
ans = list(set(ans)) # 2
ans.sort()

for l in ans[1:]: # m이 1보다 커야하므로
    print(l, end=" ")
```

