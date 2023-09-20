# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
import sys
input = sys.stdin.readline

# deposit, pay, reservation
N, M = map(int, input().split())
account = N
arr = deque()
for i in range(M):
	command, amount = map(str, input().split())
	amount = int(amount)
	
	if command == "deposit":
		account += amount
		
		while arr and arr[0] <= account:
			account -= arr.popleft()
			
	elif command == "pay":
		if (account - amount) < 0:
			account = account
		else: 
			account -= amount	
	elif command == "reservation":
		if (account - amount) < 0 or len(arr) > 0:
			arr.append(amount)
		else:
			account -= amount
			
print(account)
			
	