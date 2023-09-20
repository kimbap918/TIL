# # 14번 문제 
# s = input()
# cnt = 0
# for i in s:
#     if "a" in i:
#         cnt += 1
# print(cnt)

# # 15번 문제 
# s = "apple"
# a = list(s)
# for i in range(len(a)):
#     if "a" not in a:
#         print(-1)
#         break
#     if a[i] == "a":
#         print(i)
#         break

# # 16번 문제
# mo_list = ['a', 'e', 'i', 'o', 'u']
# s = input()
# a = list(s)
# cnt = 0
# for i in range(len(mo_list)):
#     if a[i] in mo_list:
#         cnt += 1
# print(cnt)

# # 17번 문제
# # 아스키 대문자 65~90
# s = list(input())
# a = []
# for i in range(len(s)):
#     if ord(s[i]) > 96:
#         s[i] = ord(s[i]) - 32
#         print(chr(s[i]), end='')

# # 18번 문제
# str = input()
# my_dict = {}
# for char in str:
#     if char in my_dict:
#         my_dict[char] += 1
#     else:
#         my_dict[char] = 1
# for k, v in my_dict.items():
#     print(k, v)

# 바나나가 두번 들어있어도 키나 값을 출력하면 하나만 출력됨.
# 딕셔너리의 특성을 이용하여 나온 단어 횟수를 풀수있다.
my_dict = {'banana' : '바나나', 'banana' : '바나나', 'apple' : '사과'}
print(my_dict.items())