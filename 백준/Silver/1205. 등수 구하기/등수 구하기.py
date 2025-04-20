N, S, P = map(int, input().split())

if N == 0:
    print(1)
else:
    rank = list(map(int, input().split()))
    rank.append(S)
    rank.sort(reverse=True)
    
    position = rank.index(S) + 1  # 등수는 1부터 시작

    # 랭킹이 꽉 찼고, S가 리스트의 마지막보다 작거나 같으면 못 들어감
    if N == P and rank.count(S) + rank.index(S) > P:
        print(-1)
    elif position > P:
        print(-1)
    else:
        print(position)
