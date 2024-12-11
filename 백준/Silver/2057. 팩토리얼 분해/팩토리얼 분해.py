def factorial_sum(N):
    # 0인 경우 예외 처리
    if N == 0:
        return False
    
    # 팩토리얼 미리 계산
    factorials = [1]
    i = 2
    while factorials[-1] <= N:
        factorials.append(factorials[-1] * (i-1))
        i += 1
    factorials.pop()
    
    # 메모이제이션을 위한 캐시
    memo = {}
    
    def can_make_sum(target, index):
        # 기저 케이스
        if target == 0:
            return True
        if target < 0 or index < 0:
            return False
        
        # 메모이제이션 체크
        key = (target, index)
        if key in memo:
            return memo[key]
        
        # 현재 팩토리얼 포함하거나 미포함
        result = (can_make_sum(target - factorials[index], index - 1) or 
                  can_make_sum(target, index - 1))
        
        # 결과 캐싱
        memo[key] = result
        return result
    
    return can_make_sum(N, len(factorials) - 1)

# 입력 받기
N = int(input().strip())

# 결과 출력
print("YES" if factorial_sum(N) else "NO")