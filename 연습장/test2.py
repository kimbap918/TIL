# n = int(input())
# fibo_results = [0] * (n + 1)
# fibo_results[0] = 1
# fibo_results[1] = 1

# for i in range(2, n):
# 	fibo_results[i] = fibo_results[i - 1] + fibo_results[i - 2]
	
# print(fibo_results[n-1] % 1000000007)




n = int(input())
fibo_results = [0] * (n + 1)
fibo_results[0] = 1
fibo_results[1] = 1

for i in range(2, n):
    fibo_results[i] = fibo_results[i - 1] + fibo_results[i - 2]

result = fibo_results[n - 1]
print(result % 1000000007)


