N, K = map(int, input().split())
wheel = ['?' for _ in range(N)]
arrow_idx = 0  # 현재 화살표가 가리키는 위치

possible = True
for _ in range(K):
    try:
        S, alphabet = input().split()
        S = int(S)
    except:
        # 입력이 부족한 경우 멈춤
        break
    
    # 화살표의 새 위치 계산 (시계 방향 회전)
    new_arrow_idx = (arrow_idx - S % N) % N  # 시계방향으로 S칸 회전하면 인덱스는 감소
    
    # 현재 화살표 위치의 글자 확인
    if wheel[new_arrow_idx] != '?' and wheel[new_arrow_idx] != alphabet:
        possible = False
        break
    
    wheel[new_arrow_idx] = alphabet
    
    # 바퀴 회전 후 화살표 위치 업데이트
    arrow_idx = new_arrow_idx

# 가능한 바퀴인지 확인
if not possible:
    print("!")
else:
    # 바퀴에 같은 글자가 두 번 이상 등장하는지 확인
    used_chars = {}
    for char in wheel:
        if char != '?':
            if char in used_chars:
                possible = False
                break
            used_chars[char] = True
    
    if not possible:
        print("!")
    else:
        # 마지막 화살표 위치부터 시계방향으로 바퀴 출력
        result = ''
        for i in range(N):
            result += wheel[(arrow_idx + i) % N]
        print(result)