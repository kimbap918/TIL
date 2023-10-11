case = int(input())
answer = 0

for _ in range(case):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        answer = max(answer, 10000+a*1000)
    elif a == b:
        answer = max(answer, 1000+a*100)
    elif a == c:
        answer = max(answer, 1000+a*100)
    elif b == c:
        answer = max(answer, 1000+b*100)
    else:
        answer = max(answer, 100 * max(a,b,c))

print(answer)