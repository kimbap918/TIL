from collections import deque

N = int(input())
d_que = deque()

for i in range(1, N+1):
    d_que.append(i)

# 1사이클    5
while len(d_que) != 1:
    l_pop = d_que.popleft()    
    print(l_pop, end= ' ') # 1
    l_pop = d_que.popleft() # 2
    d_que.append(l_pop) # 3, 4, 5, 2
print(d_que[0])
