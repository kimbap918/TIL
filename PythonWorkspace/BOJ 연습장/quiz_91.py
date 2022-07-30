N, M = map(int, input().split())

num = list(map(int, input().split()))
sum = 0
for i in range(len(num)):
    for j in range(i+1, N):
        for k in range(j+1, N):
            print("i :"+str(i))
            print("j :"+str(j))
            print("k :"+str(k))   
            # 카드 3장 합이 M보다 작거나 카드 3장 합이 S보다 작으면 건너뜀          
            if num[i]+num[j]+num[k] > M or num[i]+num[j]+num[k] < sum:
                continue
            # 그외에는 합산
            sum = num[i]+num[j]+num[k]
print(sum)



# maxs =10으로 잡고 

# for i in range(길이):

#     for j in range(i,길이):

#          for j in range(j,길이):

#                 if~~~~
