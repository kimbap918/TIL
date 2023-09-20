import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = dict()

for i in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in arr:
            arr[word][0] += 1
        else:
            arr[word] = [1, len(word), word]

ans = sorted(arr.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in ans:
    print(i[0])