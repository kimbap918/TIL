case = int(input()) # 테스트 케이스의 개수
group = 0 # 그룹 단어 카운트

for i in range(case): # 케이스의 개수 만큼
    word = input() # 단어 입력
    not_group = 0 # 그룹 단어가 아닌 것 카운트

    for idx in range(len(word)-1): # 범위 : 0부터 단어길이의 -1까지, index out of range 방지
        if word[idx] != word[idx+1]: # 연속된 문자가 서로 다르면
            new_word = word[idx+1:] # 현재 문자 이후의 문자열을 단어로 생성함
            if new_word.count(word[idx]) > 0:
                not_group += 1
    if not_group == 0:
        group += 1
print(group)
