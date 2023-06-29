num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
            
    per = (cnt/scores[0])*100
    print('%.3f' %per + '%')