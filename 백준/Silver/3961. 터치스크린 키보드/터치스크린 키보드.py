import sys

input = sys.stdin.readline

# 키보드 좌표 설정
keyboard_layout = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

# 키보드 위치 딕셔너리
key_pos = {char: (row, col) for row, line in enumerate(keyboard_layout) for col, char in enumerate(line)}


def get_dist(word1, word2):
    distance = 0
    for c1, c2 in zip(word1, word2):
        x1, y1 = key_pos[c1]
        x2, y2 = key_pos[c2]
        distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

t = int(input())

for _ in range(t):
    word , l = map(str, input().split())
    l = int(l)

    words = [input().strip() for _ in range(l)]

    res = sorted([(w, get_dist(word, w)) for w in words], key=lambda x: (x[1], x[0]))

    for word, distance in res:
        print(word, distance)
