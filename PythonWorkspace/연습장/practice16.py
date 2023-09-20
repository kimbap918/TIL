# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline

mod = 1_000_000_007
K = int(input())
memo = [0, 1]
def fib(n):
	if n < 2:
		return n
	else:
		for i in range(2, n+1):
			memo.append(memo[i-1] + memo[i-2])
		return memo[n]
	
print(fib(K) % mod)
				