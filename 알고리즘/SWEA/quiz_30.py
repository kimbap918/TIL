# T = int(input())

# for i in range(1, T+1):
#     num = int(input())
#     print("#{} ".format(i))
#     for n in range(num):
#         print(str(11**n))

#         # 11의 거듭제곱은 파스칼의 삼각형이다.


T = int(input())

for t in range(1, T+1):
    result = []
    n = int(input()) # 입력할 열의 값
    for i in range(n): # 01234
        print(i)
        temp = []
        for j in range(i+1): # 01 012 0123 01234..
            if j == 0 or j == i: # j가 0이 나올때나, j가 i와 같을때
                temp.append(1) # 1을 넣음
                print(temp)
            else:
                pass
        #         temp.append(result[i-1][j] + result[i-1][j-1])
        # result.append(temp)


    # print('#%d' % t)
    # for i in result:
    #     print(*i)


