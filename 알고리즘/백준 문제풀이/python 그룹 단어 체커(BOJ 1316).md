## 파이썬 그룹 단어 체커(백준 BOJ 1316)



## 문제

그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

<br>

## 출력

첫째 줄에 그룹 단어의 개수를 출력한다.

<br>

## 예제 입력 1

```
3
happy
new
year
```

## 예제 출력 1

```
3
```

## 예제 입력 2

```
4
aba
abab
abcabc
a
```

## 예제 출력 2

```
1
```

## 예제 입력 3 

```
5
ab
aa
aca
ba
bb
```

## 예제 출력 3

```
4
```

## 예제 입력 4

```
2
yzyzy
zyzyz
```

## 예제 출력 4

```
0
```

## 예제 입력 5 

```
1
z
```

## 예제 출력 

```
1
```

<br>

## 📝 풀어보기

``` python
case = int(input()) # 테스트 케이스의 개수
group = 0 # 그룹 단어 카운트

for i in range(case): # 케이스의 개수 만큼
    word = input() # 단어 입력
    not_group = 0 # 그룹 단어가 아닌 것 카운트

    for idx in range(len(word)-1): # 범위 : 0부터 단어길이의 -1까지, index out of range 방지
        if word[idx] != word[idx+1]: # 연속된 문자가 서로 다르면
            new_word = word[idx+1:] # 현재 문자 이후의 문자열을 단어로 생성함
            if new_word.count(word[idx]) > 0: # 새 문자열에서 이전 문자열의 단어가 1개이상 카운트되면
                not_group += 1 # 그룹 단어가 아님
    if not_group == 0: # 그룹 단어인 경우
        group += 1 # 그룹 카운트 + 1
print(group)
```

📌 먼저 테스트 케이스의 개수를 입력받을 변수와 그룹 단어를 카운트 할 변수를 생성한다.

``` python
case = int(input()) # 테스트 케이스의 개수
group = 0 # 그룹 단어 카운트
```

📌 테스트 케이스만큼 단어를 입력받을 수 있게 for문을 생성하고 그룹 단어가 아닌것을 입력받을 변수도 생성한다.

``` python
for i in range(case): # 케이스의 개수 만큼
    word = input() # 단어 입력
    not_group = 0 # 그룹 단어가 아닌 것 카운트
```

📌 0부터 단어 길이-1 까지 범위를 잡고`(-1가 아닌 len(word)로 하면 index out of range 오류가 발생한다.)` 입력된 단어의 첫번째와 그 다음을 비교한다. 연속된 문자가 서로 다르다면 비교한 문자 이후의 문자열을 새로 생성한다. 

새 문자열에서 이전 문자열의 단어가 1개 이상 카운트되면 `not_group` 카운트를 증가시킨다.

``` python
    for idx in range(len(word)-1): # 범위 : 0부터 단어길이의 -1까지, index out of range 방지
        if word[idx] != word[idx+1]: # 연속된 문자가 서로 다르면
            new_word = word[idx+1:] # 현재 문자 이후의 문자열을 단어로 생성함
            if new_word.count(word[idx]) > 0: # 새 문자열에서 이전 문자열의 단어가 1개이상 카운트되면
                not_group += 1 # 그룹 단어가 아님
```

📌 `not_group`의 카운트가 0인 경우 `group`의 카운트를 1 증가시키고 출력한다.

``` python
    if not_group == 0: # 그룹 단어인 경우
        group += 1 # 그룹 카운트 + 1
print(group)
```

