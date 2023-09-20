for _ in range(3):
    S = list(input())
    arr = [S[0]] # 입력값의 첫번째 글자
    answer = [1] 
    cnt = 1
    for i in range(1, 8): # 여덟자리 정수기 때문에 7번 반복
        if(arr[len(arr)-1] == S[i]): # arr에 담긴 숫자가 S[i]와 같으면
            cnt += 1 
        else:
            arr.append(S[i]) # 다르면 arr에 새 숫자 추가 
            answer.append(cnt) # 카운트 추가
            cnt = 1 # 1로 초기화
    answer.append(cnt)
    print(max(answer))