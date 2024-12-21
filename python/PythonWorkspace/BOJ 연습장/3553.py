
# Give me a positive integer number which is divisible by 
# d and has exactly n digits in it, assuming that 
# d is equal to forty-five and 
# n is equal to three!



# n의 자리수 이면서 d로 나눌수있는 양수
n, d = map(int, input().split())

# 20, 1 = 20자리의 양의 정수 중 1로 나누어 떨어지는 수
# 1, 23 = 1자리의 양의 정수 중 23으로 나누어 떨어지는 수

min_val = 10**(n-1)
max_val = 10**n-1

if min_val % d == 0:
    result = min_val
else:
    result = (min_val+d-1) // d*d

if result <= max_val:
    print(result)
else:
    print("No solution")