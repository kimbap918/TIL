## 파이썬 LCS(백준 BOJ 9251)

<br>

## 문제

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

<br>

## 입력

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

<br>

## 출력

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

<br>

## 예제 입력 1

```
ACAYKP
CAPCAK
```

## 예제 출력 1 

```
4
```

<br>

## 📝 풀어보기

입력하는 a와 b에 공백문자를 넣고 맨 오른쪽의 공백문자를 제거한다.

LCS를 담을 리스트 dp를 생성해 b의 길이만큼 0의 개수를 생성하고, a의 길이만큼   리스트를 생성한다.

첫번째 공백문자를 제외한 1부터 a, b의 길이만큼 반복하면서 a와 b가 같다면,  이전의 LCS길이에 1을 더해준다.

a와 b가 다른 경우에는 a와 b의 탐색되는 글자에서 따로 한 글자씩을 비교해서 그 중에 큰 값을 가져와 저장한다.

마지막으로 dp리스트의 배열 마지막, 끝 요소를 가져온다.

``` python
a = ' ' + input().rstrip()
b = ' ' + input().rstrip()

dp = [[0] * len(b) for _ in range(len(a))]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]: 
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1]) # 2차원 배열 마지막의 마지막 요소를 가져옴
```

