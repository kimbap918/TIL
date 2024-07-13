import sys
input = sys.stdin.readline

def newNum(num):
    num = list(num)
    while num[-1] == "0":
        del num[-1]
    return int(''.join(num)[::-1])
        
for _ in range(int(input())):
    n, m = map(str, input().split())
    
    answer = newNum(n) + newNum(m)
    print(newNum(str(answer)))