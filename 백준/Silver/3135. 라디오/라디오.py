
A, B = map(int, input().split())
# 현재 주파수 A, 목표 주파수 B
N = int(input())
# 즐겨찾기 버튼 개수

res = [abs(A-B)]

for i in range(N):
    cnt = 0
    Hz = int(input())

    while True:
        if Hz == B:
            cnt += 1
            res.append(cnt)
            break
        if Hz > B:
            Hz -= 1
            cnt += 1
        elif Hz < B:
            Hz += 1
            cnt += 1


print(min(res))
# 1. 현재 위치에서 목적지까지 이동하는 값 체크 -> 확인
# 2. 즐겨찾기 버튼 개수에 따른 각각의 카운트 체크
# 3. 최소값 찾기