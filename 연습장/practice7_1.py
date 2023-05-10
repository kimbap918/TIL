# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(str, input().split())))
ans = deque()
# 16 19 31 42

for i in range(len(arr)-1):
	if arr[i] not in ans:
		ans.append(arr[i])
	if arr[i][0] == arr[i+1][-1]:
		ans.append(arr[i+1]+arr[i][1])

if len(arr) > 2:
	ans.append(arr[-1])


print(''.join(ans))