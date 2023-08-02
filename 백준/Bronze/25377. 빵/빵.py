n = int(input())  
a_list = []
b_list = []
for _ in range(n):
    a, b = map(int, input().split()) 
    a_list.append(a)
    b_list.append(b)

time = []
for i in range(n):
    if b_list[i] >= a_list[i]:  
        time.append(b_list[i])

if time:
    print(min(time))  
else:
    print(-1) 