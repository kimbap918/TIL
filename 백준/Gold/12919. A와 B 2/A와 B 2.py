def can_transform(S, T):

    # 기저 조건: S와 T가 같은 경우
    if S == T:
        return True
    
    # T의 길이가 1 이하인 경우 더 이상 변환 불가
    if len(T) <= 1:
        return False
    
    # 경우 1: T의 마지막 문자가 'A'인 경우
    if T[-1] == 'A':
        # A를 제거하고 재귀 호출
        if can_transform(S, T[:-1]):
            return True
    
    # 경우 2: T의 첫 글자가 'B'인 경우 (주의: 첫 글자!)
    if T[0] == 'B':
        # 첫 글자 B를 제거하고 뒤집은 후 재귀 호출
        if can_transform(S, T[1:][::-1]):
            return True
    
    return False

# 메인 코드
S = input().strip()
T = input().strip()

if len(S) > len(T):
    print(0)  # S가 T보다 길면 변환 불가능
else:
    # T에서 S로의 변환이 가능한지 확인 (반대 방향으로 생각)
    if can_transform(S, T):
        print(1)
    else:
        print(0)
