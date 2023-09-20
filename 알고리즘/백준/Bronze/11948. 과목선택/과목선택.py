li = [] 
for _ in range(6):  
    li.append(int(input())) 
li1 = sorted(li[:4]) 
li2 = li[4:] 
print(sum(li1[1:]) + max(li2))