import math
# 원의 넓이(원의 반지름) X (원의 반지름) X (원주율)
# 택시 기하학 원의 넓이 2 * r^2 
R = int(input())

print("{0:.6f}".format(R*R*math.pi))
print("{0:.6f}".format(2*R**2))