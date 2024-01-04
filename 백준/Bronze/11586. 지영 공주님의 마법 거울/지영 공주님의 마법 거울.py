n = int(input())
mirror = [input() for _ in range(n)]
k = int(input())
 
if k == 1:  
    print(*mirror, sep='\n')
elif k == 2:   
    print(*[i[::-1] for i in mirror], sep='\n')
else:    
    print(*mirror[::-1], sep='\n')