import sys
import string
input = sys.stdin.readline

S = input().rstrip()
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
