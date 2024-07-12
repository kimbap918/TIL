n = int(input()) 

count = 0
k = 1

while n > 0:
    if k > n:      
        k = 1      
    n -= k         
    k += 1        
    count += 1
    
print(count)