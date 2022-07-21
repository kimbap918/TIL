case = int(input())
group = 0

for i in range(case):
    word = input() # 테스트케이스 개수
    not_group = 0

    for idx in range(len(word)-1): # 인덱스 범위 : 0부터 단어개수 -1까지
        if word[idx] != word[idx+1]: # 연속된 문자가 다르다면
            new_word = word[idx+1:] # 현재 글자 이후 문자열을 단어로 생성
            if new_word.count(word[idx]) > 0: # 남은 문자열에서 현재글자가 있었다면
                not_group += 1 # 그룹단어가 아님

    if not_group == 0:
        group += 1
print(group)
