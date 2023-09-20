# 입력
R, C, N = map(int, input().split())

# 필요한 CCTV 수
row = R//N
if R % N != 0:
    row += 1

col = C//N
if C % N != 0:
    col += 1

print(row*col)