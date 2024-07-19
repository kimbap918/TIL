N = int(input())
S = input()
Adrian = 'ABC'*(N//3)+'ABC'[:N%3]
Bruno = 'BABC'*(N//4) + 'BABC'[:N%4]
Goran = 'CCAABB'*(N//6) + 'CCAABB'[:N%6]

A = 0
B = 0
G = 0
for i in range(N):
    if S[i] == Adrian[i]:
        A += 1
    if S[i] == Bruno[i]:
        B += 1
    if S[i] == Goran[i]:
        G += 1

print(max(A,B,G))
if max(A,B,G) == A:
    print('Adrian')
if max(A,B,G) == B:
    print('Bruno')
if max(A,B,G) == G:
    print('Goran')