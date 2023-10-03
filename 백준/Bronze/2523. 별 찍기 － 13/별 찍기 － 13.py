# 변수 선언
inputNum = int(input())

# 별모양 표현 
for i in range(1,inputNum+1):
    print('*'*i)
    
for j in range(inputNum-1, 0, -1):
        print('*'*j)