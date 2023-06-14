N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
max_num = -1e9
min_num = 1e9

def DFS(plus, minus, multiple, divide, depth, total):
    global max_num, min_num
    if depth == N:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return
    else:
        if plus:
            DFS(plus-1, minus, multiple, divide, depth+1, total+A[depth])
        if minus:
            DFS(plus, minus-1, multiple, divide, depth+1, total-A[depth])
        if multiple:
            DFS(plus, minus, multiple-1, divide, depth+1, total*A[depth])
        if divide:
            DFS(plus, minus, multiple, divide-1, depth+1, int(total/A[depth]))

DFS(C[0], C[1], C[2], C[3], 1, A[0])
print(max_num)
print(min_num)
