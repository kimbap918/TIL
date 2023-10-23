# for _ in range(int(input())):
#     num = int(input())
#     res = sum(i*sum(range(i+2)) for i in range(1, num+1))
#     print(res)


for _ in range(int(input())):
    n = int(input())
    res = sum(k*sum(range(k+2)) for k in range(1, n+1))
    print(res)