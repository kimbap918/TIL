# 입력으로 주어지는 숫자 n에 따라 별 모양의 그래프를 출력
n = int(input())
# n x 2n 크기의 이차원 리스트인 graph를 생성, 이차원 리스트는 공백으로 초기화
graph = [[' '] * 2*n for _ in range(n)]


def recursive(x, y, N):
    # N이 3인 경우
    if N == 3:
        # 별 모양의 그래프를 그리기 위해 그래프의 특정 위치에 별('*')을 그리는 작업을 수행
        # 그리고 마지막으로 그래프의 가운데 줄에 별을 그림
        graph[x][y] = '*'
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            graph[x + 2][y + i] = '*'
    # 재귀적인 경우
    else:
        # 그래프를 4개의 작은 사각형으로 나누고, 각 사각형에 대해 재귀적으로 recursive 함수를 호출
        # 작은 사각형들이 계속해서 분할되어 별 모양의 그래프가 그려진다.
        nextN = N // 2
        recursive(x, y, nextN)
        recursive(x + nextN, y - nextN, nextN)
        recursive(x + nextN, y + nextN, nextN)


recursive(0, n - 1, n)
for i in graph:
    print("".join(i))