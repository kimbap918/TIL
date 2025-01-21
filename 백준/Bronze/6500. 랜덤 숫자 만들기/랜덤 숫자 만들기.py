while True:
    a0 = input().strip()
    
    if a0 == '0':  # 종료 조건
        break

    # 초기값 a0의 길이 n
    n = len(a0)
    
    # a0을 정수로 변환
    current = int(a0)
    
    # 이미 나온 값들을 추적할 set
    seen = set()
    
    while current not in seen:
        seen.add(current)
        # current 값을 제곱하고, 2*n 자리로 만들기
        square = current * current
        # 제곱한 결과를 문자열로 바꾸고 길이를 맞춰줌
        square_str = str(square).zfill(2 * n)
        # 가운데 n 자리만 추출
        current = int(square_str[n // 2:n // 2 + n])

    # 결과 출력
    print(len(seen))
