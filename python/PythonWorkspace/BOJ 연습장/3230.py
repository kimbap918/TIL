def solve_ski_medal():
    # 입력 받기
    N, M = map(int, input().split())
    
    # 첫 번째 경주 순위
    first_race = []
    for _ in range(N):
        first_race.append(int(input()))
    
    # 두 번째 경주 순위
    second_race = []
    for _ in range(M):
        second_race.append(int(input()))
    
    # 각 선수의 전체 순위 계산
    total_ranking = {}
    
    # 첫 번째 경주 순위 기록
    for i, rank in enumerate(first_race, 1):
        if i not in total_ranking:
            total_ranking[i] = rank
    
    # 두 번째 경주에 참가한 선수들의 순위 업데이트
    for i, rank in enumerate(second_race, 1):
        # 두 번째 경주 참가 선수들은 M등부터 시작
        participant = N - i + 1
        total_ranking[participant] *= rank
    
    # 순위 오름차순 정렬
    sorted_ranking = sorted(total_ranking.items(), key=lambda x: x[1])
    
    # 메달 수상자 출력
    for i in range(3):
        print(sorted_ranking[i][0])

# 메인 실행 코드
if __name__ == "__main__":
    solve_ski_medal()