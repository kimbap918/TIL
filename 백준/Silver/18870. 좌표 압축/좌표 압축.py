# 자신보다 작은 수 -> 압축좌표
import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
set_S = sorted(list(set(S)))

dic = {set_S[i] : i for i in range(len(set_S))}
# print(dic)
# print(set_S)

for i in S:
    print(dic[i], end=' ')
