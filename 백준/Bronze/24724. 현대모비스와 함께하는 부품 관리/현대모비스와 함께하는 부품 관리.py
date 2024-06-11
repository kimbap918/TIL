import sys
input = sys.stdin.readline

i = 1
for _ in range(int(input())):
    N = int(input())
    a,b = map(int, input().split())
    for _ in range(N):
        a,b = map(int, input().split())
    print("Material Management "+str(i))
    print("Classification ---- End!")
    i += 1