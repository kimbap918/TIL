def solve(N, M, votes):
    total_votes = sum(votes)
    min_votes = (total_votes + 1) // 2

    votes.sort(reverse=True)

    start, end = 0, M
    res = 0

    while start <= end:
        mid = (start+end) // 2
        budget = mid 
        votes_against = 0

        for vote in votes:
            if budget + mid > M: # 남은 예산이 부족하면
                break

            budget += mid
            votes_against += vote

            if votes_against >= min_votes:
                break

        if budget <= M and votes_against >= min_votes:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    return res

N, M = map(int, input().split())
votes = list(map(int, input().split()))


print(solve(N, M, votes))