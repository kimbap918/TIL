## 파이썬 재귀의 귀재(백준 BOJ 25501)

<br>

## 문제

정휘는 후배들이 재귀 함수를 잘 다루는 재귀의 귀재인지 알아보기 위해 재귀 함수와 관련된 문제를 출제하기로 했다.

팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다. 팰린드롬의 예시로 AAA, ABBA, ABABA 등이 있고, 팰린드롬이 아닌 문자열의 예시로 ABCA, PALINDROME 등이 있다.

어떤 문자열이 팰린드롬인지 판별하는 문제는 재귀 함수를 이용해 쉽게 해결할 수 있다. 아래 코드의 isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환하는 함수다.

```
#include <stdio.h>
#include <string.h>

int recursion(const char *s, int l, int r){
    if(l >= r) return 1;
    else if(s[l] != s[r]) return 0;
    else return recursion(s, l+1, r-1);
}

int isPalindrome(const char *s){
    return recursion(s, 0, strlen(s)-1);
}

int main(){
    printf("ABBA: %d\n", isPalindrome("ABBA")); // 1
    printf("ABC: %d\n", isPalindrome("ABC"));   // 0
}
```

정휘는 위에 작성된 isPalindrome 함수를 이용하여 어떤 문자열이 팰린드롬인지 여부를 판단하려고 한다.

구체적으로는, 문자열 S$S$를 isPalindrome 함수의 인자로 전달하여 팰린드롬 여부를 반환값으로 알아낼 것이다. 더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다.

정휘를 따라 여러분도 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.

## 입력

첫째 줄에 테스트케이스의 개수 T$T$가 주어진다. (1≤T≤1000$1 \leq T \leq 1\,000$)

둘째 줄부터 T$T$개의 줄에 알파벳 대문자로 구성된 문자열 S$S$가 주어진다. (1≤|S|≤1000$1 \leq \vert S\vert \leq 1\,000$)

<br>

## 출력

각 테스트케이스마다, isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 줄에 공백으로 구분하여 출력한다.

<br>

## 예제 입력 1 

```
5
AAA
ABBA
ABABA
ABCA
PALINDROME
```

## 예제 출력 1 

```
1 2
1 3
1 3
0 2
0 1
```

<br>

## 📝 풀어보기

📌 문제의 예시를 참고해서 recursion 함수와 isPalindrome 함수를 만든다.

cnt를 생성해서 재귀가 일어날 때마다 cnt를 1씩 증가시켜준다.

예제에서, 팰린드롬일때 1, 팰린드롬이 아닐때 0, 그외엔 함수를 다시 호출한다. isPalindrome 함수에서 입력받은 문자열 S를 `문자열 s, 0, 문자열 s의 길이-1 ` 로 반환해 recursion 함수로 넘기고, recursion에서 팰린드롬인지 아닌지 숫자로 판별한다. 

``` python
def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: 
      return 1
    elif s[l] != s[r]: 
      return 0
    else: 
      return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
```

<br>

📌 테스트 케이스 T를 입력받고 cnt를 생성한다.

T의 횟수만큼 반복하면서 문자열 S를 입력받고 isPalindrome(S)와 cnt를 출력한다.

``` python
T = int(input())
cnt = 0
for _ in range(T):
    S = input()
    print(isPalindrome(S), cnt)
    cnt = 0
```

<br>

#### 전체 코드

``` python
def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
cnt = 0
for _ in range(T):
    S = input()
    print(isPalindrome(S), cnt)
    cnt = 0
```

