# 변수명 season1으로 지정
# seasons = ['봄', '여름', '가을', '겨울']
# '겨울'일 경우에만 '아 겨울 진짜 추워 죽겠다'라고 출력
# 나머지에 대해서는 '현재 계절은 (나머지)가 아닙니다.

seasons = ['봄', '여름', '가을', '겨울']

for season1 in seasons:
    if season1 == '겨울':
        print(f'아 {season1} 진짜 추워 죽겠다')
    else:
        print(f'현재 계절은 {season1}이 아닙니다.')