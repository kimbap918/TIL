import sys
input = sys.stdin.readline

L = int(input())
M = 1234567891
string = input()
answer = 0

for i in range(L):
    answer += (ord(string[i])-96) * (31 ** i) 
print(answer % M)

