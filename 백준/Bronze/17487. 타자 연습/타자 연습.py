S = input() 
li_left = 'qwertyasdfgzxcvb' 
li_right = 'uiophjklnm' 
cnt_left, cnt_right, cnt_other = 0, 0, 0 

for i in S: 
    if i.isupper(): 
        cnt_other += 1 
         
for i in S.lower(): 
    if i in li_right: 
        cnt_right += 1 
    elif i in li_left: 
        cnt_left += 1 
    else: 
        cnt_other += 1 

while cnt_other != 0: 
    if cnt_left <= cnt_right: 
        cnt_left += 1 
    else: 
        cnt_right += 1 
    cnt_other -= 1 
     
print(cnt_left, cnt_right)