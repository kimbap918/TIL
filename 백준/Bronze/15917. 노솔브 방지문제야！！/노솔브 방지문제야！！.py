import sys
input = sys.stdin.readline

a = [2**i for i in range(32)]

for i in range(int(input())):
    print(1 if int(input()) in a else 0)