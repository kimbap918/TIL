N, Q = map(int, input().split())
song_list = []
cnt = 1
for i in range(N):
    # 1번악보 2초
    # 2번악보 1초
    # 3번악보 3초
    length = int(input())
    for j in range(length):
        song_list.append(cnt)
    cnt+=1
for j in range(Q):
    query = int(input())
    print(song_list[query])