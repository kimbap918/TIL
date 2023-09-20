## 파이썬 인간-컴퓨터 상호작용(백준 BOJ 16139)

<br>

## 문제

승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다. 

'문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'

승재를 도와 특정 문자열 S$S$, 특정 알파벳 α$\alpha$와 문자열의 구간 [l,r]$[l,r]$이 주어지면 S$S$의 l$l$번째 문자부터 r$r$번째 문자 사이에 α$\alpha$가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 승재는 문자열의 문자는 0$0$번째부터 세며, l$l$번째와 r$r$번째 문자를 포함해서 생각한다. 주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을 q$q$번 할 것이다.

<br>

## 입력

첫 줄에 문자열 S$S$가 주어진다. 문자열의 길이는 200,000$200,000$자 이하이며 알파벳 소문자로만 구성되었다. 두 번째 줄에는 질문의 수 q$q$가 주어지며, 문제의 수는 1≤q≤200,000$1\leq q\leq 200,000$을 만족한다. 세 번째 줄부터 (q+2)$(q+2)$번째 줄에는 질문이 주어진다. 각 질문은 알파벳 소문자 αi$\alpha_i$와 0≤li≤ri<|S|$0\leq l_i\leq r_i<|S|$를 만족하는 정수 li,ri$l_i,r_i$가 공백으로 구분되어 주어진다.

<br>

## 출력

각 질문마다 줄을 구분해 순서대로 답변한다. i$i$번째 줄에 S$S$의 li$l_i$번째 문자부터 ri$r_i$번째 문자 사이에 αi$\alpha_i$가 나타나는 횟수를 출력한다.

<br>

## 서브태스크 1 (50점)

문자열의 길이는 2,000$2,000$자 이하, 질문의 수는 2,000$2,000$개 이하이다.

<br>

## 서브태스크 2 (50점)

추가 제한 조건이 없다.

<br>

## 예제 입력 1

```
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10
```

## 예제 출력 1

```
0
1
2
1
```

<br>

## 📝 풀어보기

📌 문자열 S를 입력받는다.

질문의 수 q를 입력받고 알파벳을 담아놓을 딕셔너리 alphabet을 생성한다. 

string을 import받아 string.ascii_lowercase의 소문자들을 alphabet에 저장한다.

cnt를 생성하고 S의 길이만큼 반복하면서 S[i]와 문자가 같으면 카운트를 증가시키고 alphabet 딕셔너리의 해당 문자에 증가한 카운트 값을 저장한다.

``` python
import sys
import string
input = sys.stdin.readline

S = input()
q = int(input())
alphabet = {}
for char in string.ascii_lowercase:
    alphabet[char] = [0]
    cnt = 0
    for i in range(len(S)):
        if S[i] == char:
            cnt += 1
        alphabet[char].append(cnt)
```

<br>

📌 질문의 수만큼 반복하면서 찾는문자, 시작, 끝점을 입력받고 그 중 시작과 끝점은 int로 형변환한다.

alphabet `딕셔너리의[찾는문자][끝점]` 에서  `딕셔너리의[찾는문자][시작점]` 을 뺀 값을 출력한다.

``` python
for _ in range(q):
    a,l,r = input().split()
    l,r = int(l), int(r)
    print(alphabet[a][r+1] - alphabet[a][l])
```

<br>

#### 전체 코드

``` python
import sys
import string
input = sys.stdin.readline

S = input()
q = int(input())
alphabet = {}
for char in string.ascii_lowercase:
    alphabet[char] = [0]
    cnt = 0
    for i in range(len(S)):
        if S[i] == char:
            cnt += 1
        alphabet[char].append(cnt)

for _ in range(q):
    a,l,r = input().split()
    l,r = int(l), int(r)
    print(alphabet[a][r+1] - alphabet[a][l])
```

