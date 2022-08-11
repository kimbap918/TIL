directions = {
    # x, y 좌표
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}
# 킹의 위치, 돌의 위치, 움직이는 횟수
K, S, N = input().split() # A1 H8 1
kx, ky = 8 - int(K[1]), ord(K[0])-65 # 8 - 1 = 7 / A(65) - 65 = 0 (7, 0)
sx, sy = 8 - int(S[1]), ord(S[0])-65 # 8 - 2 = 6 / A(65) - 65 = 0 (0, 0)
for _ in range(int(N)): # 움직이는 횟수
    cmd = input().strip()
    dx, dy = directions[cmd] # T (-1, 0)
    # 킹이 체스판 범위를 벗어나는 경우
    if not (0 <= kx+dx < 8 and 0 <= ky+dy < 8):
        continue # 건너뜀
    kx += dx # 킹 x 좌표에 커맨드 좌표를 더함
    ky += dy # 킹 y 좌표에 커맨드 좌표를 더함
    if (kx, ky) == (sx, sy): # 킹의 좌표와 돌의 좌표가 같을경우 
        # 돌의 좌표가 체스판을 벗어나는 경우
        if not (0 <= sx+dx < 8 and 0 <= sy+dy < 8):
            kx -= dx # 킹의 좌표에 커맨드 좌표를 무른다
            ky -= dy # 킹의 좌표에 커맨드 좌표를 무른다
            continue # 건너뜀
        sx += dx # 돌의 x좌표에 커맨드 좌표를 넣는다
        sy += dy # 돌의 y좌표에 커맨드 좌표를 넣는다

print(chr(65+ky)+str(8-kx)) # 숫자 A에 킹의 y 좌표를 더한 값 + 8에 킹의 x좌표를 뺀 값
print(chr(65+sy)+str(8-sx)) # 숫자 A에 돌의 y 좌표를 더한 값 + 8에 돌의 x좌표를 뺀 값