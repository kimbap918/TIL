n, m = map(int, input().split()) # 1부터 N까지 자연수를 나열했을때, 중복없이 M개를 고른 수열

visit = [0]*(n+1) # 자연수 크기+1 만큼 리스트 생성
arr = [0]*(m+1) # 수열 길이 +1만큼 리스트 생성

def is_not_visit(num): # 방문 확인 함수 
    if visit[num] == 0: # 방문이 없으면
        return True # 1
    else:
        return False # 0

def check(x):
    if x == m+1: # 들어온 값이 수열 길이+1과 같다면
        for i in range(1, m+1): # 1부터 m+1까지 
            print(arr[i], end=' ') # arr[i]값 출력
        print()
    else: # 다르다면 
        for i in range(1, n+1): # 1부터 n+1까지
            if is_not_visit(i): # 해당 index 방문이 없으면
                visit[i] = 1 # 1로 변경
                arr[x] = i # i로 변경
                check(x+1) # check(x+1) 실행
                arr[x] = 0 # 다음 수 출력을 위한 방문 초기화
                visit[i] = 0

check(1)