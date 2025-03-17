N, K = map(int, input().split())
X = list(map(int, input().split()))
cnt = 0 # 박수
i = 0 # 오리의 인덱스
# 오리가 소리낸 X+K 초 

while i < N:
    cnt += 1
    clap_time = X[i] + K # 가장 늦은 박수 타이밍

    while i < N and X[i] <= clap_time:
        i += 1

    
print(cnt)



# 4 > 3

# 1 + 3 = 4
# 3 + 3 = 6
# 7 + 3 = 10


# 5 3
# 1 2 3 6 8

