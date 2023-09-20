N, M = map(int, input().split()) # N * M 보드
original = [] # 원래 판을 저장하기 위한 리스트
count = [] # 바뀐 체스판의 개수를 저장하기 위한 리스트

for _ in range(N):
    original.append(input()) # original에 원래 판을 저장

for a in range(N-7): # 전체 체스판에서 시작점을 잡기위함
    for b in range(M-7):
        index1 = 0
        index2 = 0
        # 전체 체스판 중 아무곳에서나 8*8을 잘라내 최소로 칠할 값을 구하면됨
        for i in range(a, a+8): # 시작점 a를 기준으로 8칸 모두 체크
            for j in range(b, b+8): # 시작점 b를 기준으로 8칸 모두 체크
                # 0, 0 1 2 3 4 5 6 7
                # 1, 0 1 2 3 4 5 6 7...
                if (i+j) % 2 == 0: # i+j 합이 짝수인 경우
                    if original[i][j] != "W":
                        index1 += 1
                    if original[i][j] != "B":
                        index2 += 1
                else:
                    if original[i][j] != "B":
                        index1 += 1
                    if original[i][j] != "W":
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))
