import sys
input = sys.stdin.readline

arr = [ input().rstrip() for i in range(28) ]
not_in = []
for i in range(1, 31):
    if str(i) not in arr:
        not_in.append(i)

not_in.sort()        
print(not_in[0])
print(not_in[1]) 