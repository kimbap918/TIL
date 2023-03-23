# 소수 판별(비효율적)
# def primenumber(a):
#   for i in range(2, a):
#       if a % i == 0:
#           return false


# 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기자신의 제곱근(루트)까지만 확인하면 된다
# def primenumber(a):
#   for i in range(2, int(math.sqrt(x)+1)):
#       if a % i == 0:
#           return False
#   return True

import math

import sys
input = sys.stdin.readline

def is_prime(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    while True:
        if is_prime(n) == True:
            print(n)
            break
        else:
            n += 1