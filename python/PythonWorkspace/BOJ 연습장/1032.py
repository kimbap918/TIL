# 알파벳 . ?
# ?는 최대한 적게 사용
import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    words = input().rstrip()
    arr.append(words)

for i in range(len(arr)+1):
    print(arr[i])