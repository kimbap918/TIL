import sys
input = sys.stdin.readline


def maxSize():
    # 히스토그램의 최대 넓이 저장
    max_size = 0 
    stack = []
    cnt = 0
    for i in range(N):
        # 왼쪽으로 이어질 수 있는 최소의 index
        min_point = i
        # 히스토그램의 요소 값보다 stack의 각 요소 내 첫번째 요소가 크거나 같을때까지
        # 즉, 히스토그램의 요소를 전부 순회할때까지 
        # cnt += 1
        # print(cnt)
        # stack의 높이 값이, 입력한 히스토그램의 값보다 작아지면 종료 
        while stack and stack[-1][0] >= histogram[i]:
            print(stack)
            print("stack[-1][0] : "+str(stack[-1][0]), "histogram[i] : "+str(histogram[i]))
            # pop되었다는 것은 추가 될 직사각형보다 높이가 높다는 의미이다.
            # 이전의 값이 현재 값보다 높으면 직사각형이 확장될 수 없기때문에
            # 따라서 추가될 직사각형은 pop되는 직사각형의 point값까지 넓어질 수 있다
            # pop된 사각형의 point값으로 min_point를 업데이트
            h, min_point = stack.pop() # 높이, 인덱스 값은 pop된 값으로 갱신
            # print("h : "+str(h))
            # print("min_point : "+str(min_point))
            # print(stack)
            tmp_size = h * (i-min_point) # 높이 * (현재 인덱스 - 왼쪽으로 이어질 수 있는 인덱스)
            max_size = max(max_size, tmp_size) # 직사각형의 최대 높이
        # 스택에 [히스토그램의 값, 왼쪽으로 이어지는 index]를 왼쪽부터 차례로 입력, 
        stack.append([histogram[i],min_point])
        # print("min :" + str(min_point))
        # print(stack)

    #탐색이 끝나고 아직 Stack에 남은 직사각형 정보로 maxSize 갱신
    for h, point in stack:
        max_size = max(max_size, (N-point)*h)

    return max_size

while True:

    N, *histogram = map(int, input().split())
    if N == 0: 
        break
    print(maxSize())