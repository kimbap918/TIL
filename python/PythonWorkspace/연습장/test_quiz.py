N = int(input())
S = list(input().rstrip())

a_list=[a for a in S[::2]]
n_list=[int(n) for n in S[1::2]]

ans=[]

for i in range(N//2):
	plus=ord(a_list[i]) + n_list[i]**2
	if plus <= 122:
		ans.append(chr(plus))
	elif plus >122:
		ans.append(chr((plus-77) % 26 + 77))
print(''.join(ans))