# 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임
# 문자열의 뒤에 A를 추가한다.
# 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

# S = input()
# T = input()

# def word_maker(S, T):
#     res = False

#     if T == S:
#         return True

#     if len(T) < len(S):
#         return False

    
#     if T[-1] == "A":
#         res = word_maker(S, T[:-1])
#         if res:
#             return True

#     if T[-1] == "B":
#         revWord = T[:-1][::-1]
#         res = word_maker(S, revWord)
#         if res:
#             return True

#     return res


# if word_maker(S, T) == True:
#     print(1)
# else:
#     print(0)

# def word_maker(S, T):
#     """
#     주어진 문자열 T에서 연산을 통해 S로 만들 수 있는지 확인하는 함수
    
#     연산 (역으로 생각):
#     1. 문자열의 마지막이 A인 경우, A를 제거한다.
#     2. 문자열의 마지막이 B인 경우, B를 제거하고 문자열을 뒤집는다.
    
#     역방향으로 T에서 S를 만드는 방식으로 접근
#     """
#     # 기저 조건: T와 S가 같으면 변환 가능
#     if T == S:
#         return True
    
#     # T의 길이가 S보다 짧으면 불가능
#     if len(T) < len(S):
#         return False
    
#     result = False
    
#     # 경우 1: T의 마지막 문자가 'A'인 경우, A를 제거
#     if T[-1] == 'A':
#         result = word_maker(S, T[:-1])
#         if result:
#             return True
    
#     # 경우 2: T의 마지막 문자가 'B'인 경우, B를 제거하고 뒤집기
#     if T[0] == 'B':
#         # 마지막 B를 제거하고 나머지를 뒤집음
#         reversed_T = T[:-1][::-1]
#         result = word_maker(S, reversed_T)
#         if result:
#             return True
    
#     return False

# # 메인 코드
# S = input()
# T = input()

# # T에서 S로 만들 수 있는지 확인 (역방향 접근)
# if word_maker(S, T):
#     print(1)
# else:
#     print(0)

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
