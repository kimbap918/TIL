t = int(input())
for i in range(t) :
    input()	# 각 테스트 케이스는 줄 바꿈으로 구분
    N, M = map(int, input().split())
    sj = sorted(list(map(int, input().split())), reverse=True)
    sb = sorted(list(map(int, input().split())), reverse=True)
    
    while sj and sb :	# 세준, 세비 병사 리시트가 비어있으면 while문 종료
        if sj[-1] >= sb[-1] :	# 같거나 크면 세비의 병사 죽음
            sb.pop()
        else :
            sj.pop()
    
    if sj :
        print('S')
    elif sb :
        print('B')
    else :
        print('C')