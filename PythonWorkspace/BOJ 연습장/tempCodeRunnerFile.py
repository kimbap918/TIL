N, M = map(int, input().split())

poket_dic = {input() : str(i) for i in range(1, N+1)}

for j in range(M):
    S = input()
    for k, v in poket_dic.items():
        if S == k:
            print(v)
        elif S == v:
            print(k)