# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = input().rstrip()
stack = deque()
stack.append(['', 1])

# 문자열의 끝을 체크하기 위함
words += 'z' 
for word in words:
    # stack의 마지막에 저장된 단어가 순회중인 단어와 같지 않다면
    if stack[-1][0] != word:
        # stack의 마지막에 저장된 단어의 길이가 M보다 크거나 같다면
        if M <= stack[-1][1]:
            # top에 해당 단어 저장
            top = stack[-1][0]
            # top과 해당 단어가 같아질때까지 
            while top == stack[-1][0]:
                stack.pop()
    # 스택의 마지막 단어가 word와 같다면
    if stack[-1][0] == word:
        # 길이값에+1을 더한 값을 저장
        stack.append([word, stack[-1][1] + 1])
    else:
        # 길이가 1인 값을 저장
        stack.append([word, 1])
stack.pop()

if len(stack) > 1:
    for word, num in stack:
        print(word, end='')
else:
    print("CLEAR!")