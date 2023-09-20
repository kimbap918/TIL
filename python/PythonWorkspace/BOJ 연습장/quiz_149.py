# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# prefix_sum = [0]
# temp = 0

# for i in arr:
#     temp += i
#     prefix_sum.append(temp) # 구간 합의 값을 미리 저장해둠


# for j in range(M):
#     n, m = map(int, input().split())
#     print(prefix_sum[m] - prefix_sum[n-1])
    
import math
# 원의 넓이(원의 반지름) X (원의 반지름) X (원주율)
# 택시 기하학 원의 넓이 2 * r^2 
R = int(input())

print("{0:.6f}".format(R*R*math.pi))
print("{0:.6f}".format(2*R**2))
