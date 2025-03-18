def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 +1):
        comp = ''
        prev = s[0:step] # 0부터 스텝만큼 추출
        cnt = 1
        
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                comp += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+step]
                cnt = 1
        comp += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(comp))
        
    return answer
        
       
        