# 수첩 2의 M개 숫자 순서대로 
# 수첩 1에 있으면 1, 없으면 0 출력
T = int(input())

for i in range(T):
    N = int(input())
    note1 = set(map(int, input().split())) # 중복제거 
    M = int(input())
    note2 = list(map(int, input().split())) # 리스트, 순서대로 출력하기 위해

    for j in note2:
        if j in note1:
            print(1)
        else:
            print(0)
