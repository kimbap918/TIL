import sys
import string
input = sys.stdin.readline

# 1. 원문은 N/2의 길이를 가지고 있으며, 모두 알파벳 소문자이다.
# 2. 암호문의 첫 번째 문자부터 순서대로 아래의 복호화 과정을 거친다. 
# 첫 번째 문자는 문장의 가장 왼쪽 문자를 의미한다.
# 3. i가 홀수일 때, 암호문의 i번째 문자를 알파벳의 사전 기준 다음 문자로 바꾸는 작업을 암호의 i+1번째 수의 제곱 번 시행한다.
# 작업이 끝난 뒤 변환된 알파벳을 원문의 맨 오른쪽에 추가한다.
# 4. z에서 다음 문자로 바꿔야 하는 경우에는 a로 바뀌게 된다.

alphabet = list(string.ascii_lowercase)
N = int(input())
S = input().rstrip()
ans = []
for i in range(0, N, 2):
    letter, num = S[i], int(S[i+1])
    decode = (alphabet.index(letter)+(num**2)) % len(alphabet)
    ans.append(alphabet[decode])
print(''.join(ans))
