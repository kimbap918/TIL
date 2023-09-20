s = input()
A = []
B = list(s)
C = []
for i in range(97, 123):
    A.append(i)
    C.append(i)

for j in range(len(s)):
    for k in range(len(A)):
        if ord(B[j]) == A[k]: # 입력값의 리스트가 스트링을 담아놓은 리스트의 값과 같다면
            A[k] = B.index(B[j])

for i in range(len(A)):
    if A[i] == C[i]:
        A[i] = -1
    print(A[i], end=' ')

# 아스키 a=97, b=98
# baekjoon
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# a b c  d  e  f  g . . .