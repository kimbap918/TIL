import sys
input = sys.stdin.readline
T = int(input())

def min_(x,y):
    while y:
        x, y = y, x%y
        # print("x, y : "+ str(x), str(y))
        min = A*B/x
    print(int(min))

for _ in range(T):
    A, B = map(int, input().split())
    min_(A, B)