# 5
# 6 9 5 7 4 (왼쪽으로 발사)

# 0 0 2 2 4

# 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 
# 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다. 
# 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다

N = int(input())
towers = list(map(int, input().split()))
stack = []
res = [0] * N 

for i, j in enumerate(towers): # (0,6) (1,9) (2,5) (3,7) (4,4)

    while stack and stack[-1][1] < towers[i]: 
        stack.pop()

    if stack:
        res[i] = stack[-1][0]

    stack.append((i+1, j))


print(' '.join(map(str, res)))