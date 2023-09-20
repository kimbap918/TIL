
# import sys

# def cantor(arr, start, length):
#     temp = length // 3 # 길이를 3 나눈 몫 27//3 = 9
#     if temp == 0:
#         return
#     for i in range(start+temp, start+temp*2):
#         arr[i] = ' '
#     cantor(arr, start, temp)
#     cantor(arr, start+temp*2, temp)


# while True:
#     try:
#         N = sys.stdin.readline()
#         if N == '':
#             break
#         else:
#             N = int(N) # N값 입력
#             arr = ['-' for i in range(3**N)] # 3**N 만큼 - 생성
#             cantor(arr, 0, 3**N)
#             ans = ''
#             for i in arr:
#                 ans += i
#             print(ans)
#     except EOFError:
#         break

# input()은 내장 함수로 취급되는 반면, sys에 속하는 메소드들은 file object로 취급된다.
import sys
for i in sys.stdin: # ex) 3이면 i = 3
    line = "-"
    for j in range(int(i)):
        # 1회 - -
        # 2회 - -   - -
        # 3회 - -   - -         - -   - -
        line = line+" "*len(line)+line
    print(line)