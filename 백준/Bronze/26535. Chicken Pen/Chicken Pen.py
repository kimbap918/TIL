def get_pen_size(chickens):
    if chickens == 1:
        return 3 
    size = 1

    while (size-2) * (size-2) < chickens:  # 내부 공간 계산
        size += 1
    return size

def draw_pen(size):
    # 첫 줄
    print('x' * size)
    
    # 중간 줄들
    for _ in range(size-2):
        print('x' + '.' * (size-2) + 'x')
    
    # 마지막 줄
    if size > 1:  # size가 1보다 클 때만 마지막 줄 출력
        print('x' * size)

# 메인 로직
N = int(input())  # 닭의 수 입력
size = get_pen_size(N)  # 필요한 닭장 크기 계산
draw_pen(size)  # 닭장 그리기