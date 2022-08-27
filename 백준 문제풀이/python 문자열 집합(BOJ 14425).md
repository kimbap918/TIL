## 파이썬 문자열 집합(백준 BOJ 14425)

<br>

## 문제

총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. 

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

<br>

## 출력

첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

<br>

## 예제 입력 1 

```
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
```

## 예제 출력 1

```
4
```

<br>

## 📝 풀어보기

📌 입력을 readline으로 받고 N개의 수와 검사할 M개의 수를 입력받는다.

dic_N에 N만큼 반복하면서 문자열을 넣는다.

``` python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic_N = {input():0 for _ in range(N)}
```

<br>

📌 M만큼 반복하면서 문자열을 입력받고 문자열이 딕셔너리에 포함이 되어있으면 값을 1 증가시킨다. 

dic_N.values()의 값을 순회하면서 sum에 누적시키고 출력한다.

``` python
for _ in range(M): 
    S = input()
    if S in dic_N:
        dic_N[S] += 1
sum = 0
for v in dic_N.values():
    sum += v
    
print(sum)
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic_N = {input():0 for _ in range(N)}
for _ in range(M): 
    S = input()
    if S in dic_N:
        dic_N[S] += 1
sum = 0
for v in dic_N.values():
    sum += v
    
print(sum)
```

