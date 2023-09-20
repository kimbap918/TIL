n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)] # 문제의 인덱스가 1부터 시작해서 n + 1
visited = [False] * (n + 1) # 왔던곳을 확인할 변수
total = set()

# 인접리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

"""
graph = [
    [],
    [2, 5],
    [1, 3, 5],
    [2],
    [7],
    [1, 2, 6],
    [5],
    [4]
]
"""
# visited = [False] * n

def dfs(start):
    stack = [start] # stack = [1]
    # print(stack)
    visited[start] = True # visited[1] = True

    while stack:
        # pop이 맨 마지막에 추가된 요소를 가져오므로 2가 아닌 5가 빠져나간다.
        cur = stack.pop() # 1 stack.append 끝나고 -> 5
        # print("cur :"+str(cur))

        for adj in graph[cur]: # graph[1] = [2, 5]
            # print("adj :"+str(adj))
            if not visited[adj]: # visited[2] = False / visited[5] = False
                visited[adj] = True # visited[2] = True / visited[5] = False
                stack.append(adj) # stack.append(2) / stack.append(5)
                total.add(adj)
    return total
print(len(dfs(1)))
# 최종적으로 1번 컴퓨터에 의해 감염되는 컴퓨터는 2, 3, 5, 6