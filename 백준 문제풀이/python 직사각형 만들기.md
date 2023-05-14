

## 파이썬 직사각형 만들기(goorm level)

<br>
<img width="1596" alt="스크린샷 2023-05-14 오후 3 47 43" src="https://github.com/kimbap918/TIL/assets/75712723/a9515846-c138-4382-9a30-b11202d6af21">

<img width="1597" alt="스크린샷 2023-05-14 오후 3 47 59" src="https://github.com/kimbap918/TIL/assets/75712723/98d2b0d5-2043-4cc6-9270-2eced394169b">

<br>

## 📝 풀어보기 

그리디와 좀 더 친해져야겠다.

<br>

이 문제를 처음 풀때에 든 생각은 일단 무조건 같은 숫자의 쌍이 모여야 하니, **정렬을 해서 같은쌍을 쉽게 골라내려고** 했다. 그래서 입력받아 저장하는 S를 크기가 큰 순으로 정렬해서 저장했다.

그렇다면 정렬이 된 리스트에서 같은쌍을 골라서 모으면 되는데 처음에는 for 문으로 정렬된 리스트 S의 요소를 순회하면서 S[i] 와 S[i+1]을 비교하고, 두개의 비교대상이 같다면 새 리스트에 값을 저장해서 연산을 하려고했으나..

``` python
for i in range(len(S)-1):
  if S[i] == S[i+1]:
    arr.append([S[i], S[i+1]]) # 이런식으로
```

<br>

조금만 생각해보면 문제점이 보인다. 예를들어보자.

``` python
# S의 정렬된 값이 [1, 1, 2, 4, 4, 4] 라면?
arr = [[1, 1] [4, 4] [4, 4]]
```

이 문제에서 직사각형을 만드려면 항상 짝수의 같은 길이 막대가 있어야 한다.

하지만 위의 방법으로 막대를 골라내면 S에 요소가 3개인 4가 arr에 1번만 들어가야하는데 2번 들어가버리게 된다.

이것을 해결하기 위해 **딕셔너리로 요소와 요소의 개수를 저장**했다.

<br>

``` python
import sys
import collections
input = sys.stdin.readline

N = int(input())
S = sorted(list(map(int, input().split())), reverse=True)
dic = collections.Counter(S)
square = collections.deque()
ans = 0
```

여기서 square는 골라낸 길이가 같은 짝을 담아두는 리스트이고, ans는 연산의 최종값을 담아내는 변수다.

<br>

저장된 S에 대한 딕셔너리에는 값이 이런식으로 저장되어 있을것이다.

``` python
# S의 정렬된 값이 [1, 1, 2, 4, 4, 4] 라면? 
dic = Counter({4: 3, 1: 2, 2: 1})
```

콜론(:)을 기준으로 왼쪽은 키(key), 오른쪽은 값(value)이다.

4가 3개, 1이 2개, 2가 1개 들어있다.

<br>

딕셔너리의 키와 값을 순회하면서 값(요소의 개수)를 2로 나눈 몫이 1보다 크거나 같으면

**요소의 개수를 2로 나눈 몫만큼 square에  해당 키(요소)를 삽입**한다.

이렇게 하면 홀수일때 중복으로 넣지않고 짝수일때는 나눠떨어지니 해당 몫만큼 요소를 짝지어 삽입할 수 있다.

그리고 삽입된 square 리스트를 1번째 인덱스부터, square의 길이까지, 2칸씩 탐색하면서

해당 요소와, 그 이전 요소를 곱한 값을 ans에 누적시킨다. 

``` python
for k, v in dic.items():
    if (v // 2) >= 1:
        for i in range(v//2):
            square.append(k)

for i in range(1, len(square), 2):
    ans += (square[i]*square[i-1])
```

<br>

#### 전체코드

``` python
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
import collections
input = sys.stdin.readline

N = int(input())
S = sorted(list(map(int, input().split())), reverse=True)
dic = collections.Counter(S)
square = collections.deque()
ans = 0

for k, v in dic.items():
    if (v // 2) >= 1:
        for i in range(v//2):
            square.append(k)

for i in range(1, len(square), 2):
    ans += (square[i]*square[i-1])

print(ans)
```

<br>

이 문제의 해설에 적힌 답은 아래와 같다.

#### 해설

``` python
import sys
input = sys.stdin.readline

N = int(input())
pair = []
cnt = [0 for _ in range(1000001)]
sticks = map(int, input().split())
for stick in sticks:
    cnt[stick] += 1

for length in range(1, 1000001):
    while cnt[length] > 1:
        cnt[length] -= 2
        pair.append(length)

pair.sort(reverse=True)
ans = 0
for i in range(1, len(pair), 2):
    ans += pair[i - 1] * pair[i]

print(ans)
```

<br>

문제의 해설에서 나온대로, 그리디 알고리즘으로 푸는 문제는, 문제를 접근하는 방식과 증명은 어떤 식으로 할 수 있는지에 대한 직관을 필요로 하는것 같다.

