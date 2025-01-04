from collections import Counter

word = input()
cnt = Counter(word)  # 문자의 종류와 개수를 딕셔너리 형태로 저장

odd_cnt = sum(1 for c in cnt.values() if c % 2 == 1)

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
    exit(0)

half = []
middle = []

# 문자들을 사전순으로 정렬하여 처리
for char in sorted(cnt.keys()):
    freq = cnt[char]
    if freq % 2 == 1:
        middle.append(char)  # 홀수번 등장한 문자 중 중간에 배치할 문자
    half.append(char * (freq // 2))  # 문자의 절반을 앞에 배치

half = ''.join(half)
print(half + ''.join(middle) + half[::-1])
