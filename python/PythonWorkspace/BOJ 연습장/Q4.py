
N = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 1


for i in arr: # 1 1 2 3 9
    if cnt < i: #    
        break
    cnt += i 

print(cnt)




# 3 2 1 1 9

# 1 1 2 3 9