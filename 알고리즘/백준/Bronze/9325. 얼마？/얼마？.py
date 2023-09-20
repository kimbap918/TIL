T = int(input())

for _ in range(T):
    op_pri = 0
    s = int(input()) # 자동차 가격
    n = int(input()) # 옵션의 개수
    for option in range(n):
        q, p = map(int, input().split()) # 옵션의 개수와 가격
        op_pri += q * p
    print(s+op_pri) 

