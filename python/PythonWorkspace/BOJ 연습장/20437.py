import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    wordDict = {}
    W = input().rstrip()
    K = int(input())

    for i in range(len(W)):
        if W[i] not in wordDict:
            wordDict[W[i]] = [i]
        else:
            wordDict[W[i]].append(i)


    min_length = 1e9
    max_length = -1

    for char, indices in wordDict.items():
        if len(indices) < K: # 단어 등장 횟수가 K개수를 만족하지 못할때
            continue
        
        # K개씩 잘라가며 탐색
        for i in range(len(indices) - K +1):
            start = indices[i]
            end = indices[i+K-1]
            length = end - start +1
            
            min_length = min(min_length, length)
            max_length = max(max_length, length)

    if min_length == 1e9 or max_length == -1:
        print(-1)
    else:
        print(f'{min_length} {max_length}')

