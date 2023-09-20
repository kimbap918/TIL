# import sys

# input = sys.stdin.readline
# word_length, message_length = map(int,input().split())
# word = input().rstrip()
# message = input().rstrip()

# while word in message:
#     message = message.replace(word, '')

#     if message:
#         print(message)
#     elif len(message) == 0:
#         print('EMPTY')


import sys

input = sys.stdin.readline
word_length, message_length = map(int,input().split())
word = input().rstrip()
message = input().rstrip()

while word in message: 
    message = message.replace(word, '')
    print(message)

if message:
    print(message)
else:
    print('EMPTY')
# -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# import sys
# input = sys.stdin.readline

# len_S, len_E = map(int, input().split())
# S = input().rstrip()
# E = input().rstrip()
# stack = []

# for i in range(len_E):
# 	stack.append(E[i])
	
# 	if ''.join(stack[-len_S:]) == S:
# 		for _ in range(len_S):
# 			stack.pop()
		
# if stack:
# 	print(''.join(stack))
# else:
# 	print("EMPTY")