def solution(s):
    answer = len(s)  # 압축 전 원래 문자열 길이 (최대값)
    
    # step: 1부터 문자열 길이의 절반까지 시도 (반보다 긴 패턴은 반복될 수 없음)
    for step in range(1, len(s) // 2 + 1):
        comp = ''  # 압축된 결과 문자열
        prev = s[0:step]  # 첫 번째 패턴 (초기값 설정)
        cnt = 1  # 반복 횟수 카운트

        # 🔽 여기서 문자열을 step만큼 건너뛰며 확인
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:  # 이전 패턴(prev)과 현재 부분 문자열이 같다면
                cnt += 1  # 반복 횟수 증가
            else:  
                # 🔹 압축 결과 문자열에 추가 (2번 이상 반복이면 숫자 포함)
                comp += str(cnt) + prev if cnt >= 2 else prev  
                prev = s[j:j + step]  # 새로운 패턴 설정
                cnt = 1  # 카운트 초기화

                # s = "ababcdcd"
                # step = 2

                # for j in range(0, len(s), step):
                #     print(s[j:j + step])


                # s[0:2] → "ab"
                # s[2:4] → "ab"
                # s[4:6] → "cd"
                # s[6:8] → "cd"
                
        # 🔹 마지막 남은 부분도 추가
        comp += str(cnt) + prev if cnt >= 2 else prev  

        # 🔹 최소 압축 길이 갱신
        answer = min(answer, len(comp))

    return answer
