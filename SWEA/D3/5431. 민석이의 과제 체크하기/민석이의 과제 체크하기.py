T = int(input())

for _ in range(1, T+1):
    N, K = map(int, input().split()) # N 수강생의 수, K 과제를 제출한 사람의 수
    submit = list(map(int, input().split())) # 과제를 제출한 사람의 수
    a = []
    b = []

    for i in range(1, N+1): # 1부터 N+1까지 
        a.append(i)

    for j in range(len(a)):
        if a[j] not in submit:
            b.append(str(a[j]))

    print("#{} {}".format(_, ' '.join(b)))

