# 어떤 이모티콘도 포함되어 있지 않으면, none 을 출력한다.
# 행복한 이모티콘과 슬픈 이모티콘의 수가 동일하게 포함되어 있으면, unsure 를 출력한다.
# 행복한 이모티콘이 슬픈 이모티콘보다 많이 포함되어 있으면, happy 를 출력한다.
# 슬픈 이모티콘이 행복한 이모티콘보다 많이 포함되어 있으면, sad 를 출력한다.

S = input()
cnt, cnt1 = 0, 0

cnt = S.count(":-)")
cnt1 = S.count(":-(")

if cnt > cnt1:
    print("happy")
elif cnt < cnt1:
    print("sad")
    
if cnt == 0 and cnt1 == 0:
    print("none")
elif cnt == cnt1:
    print("unsure")
