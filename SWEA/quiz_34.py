T = int(input())

for _ in range(1, T+1):
    rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K = map(int, input().split())
    score_list = []
    

    for n in range(N):
        st, nd, rd = map(int, input().split())
        score = (st * 0.35 + nd * 0.45 + rd * 0.2)
        score_list.append(score)
    
    k_score = score_list[K-1] # 학생 K의 스코어
    score_list.sort(reverse=True) # 10명 학생의 성적 높은순 나열
    # [99.45, 96.25, 92.55000000000001, 88.8, 85.85000000000001, 85.75, 85.5, 74.6, 72.35, 68.95]

    div = N//10 # 학생 수를 10으로 나눈 몫
    # 10 // 10 = 1
    result = score_list.index(k_score) // div  # score_list에서 k_score index값을 찾고 몫을 구한다.
    # 2(0, 1, 2<번째) // 1 = 2
    print("#{} {}".format(_, rank[result])) # rnak[2] = A-
