stack = []
for i in range(int(input())):
    N = int(input())
    
    if N != 0:
        stack.append(N)
    else:
        stack.pop() 
print(sum(stack))
