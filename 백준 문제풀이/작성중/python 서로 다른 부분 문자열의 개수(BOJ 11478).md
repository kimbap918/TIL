## 파이썬 서로 다른 부분 문자열의 개수(BOJ 11478)

<br>

## 문제

문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

<br>

## 입력

첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

<br>

## 출력

첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.

<br>

## 예제 입력 1

```
ababc
```

## 예제 출력 1

```
12
```

<br>

## 📝 풀어보기 

``` python
S = input()
set_S = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j+1]
        set_S.add(temp)
print(len(set_S))
```

