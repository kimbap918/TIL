N = int(input())

def one(N):
    cnt = 0
    remain = 8
    if N >= 200 and N <= 209:
        while N < 209 and remain != 0:
            N += 1
            cnt += 1
            remain -= 1
    return cnt

def two(N):
    cnt = 0
    remain = 4
    if N >= 200 and N <= 219:
        while N < 219 and remain != 0:
            N += 1
            cnt += 1
            remain -= 1
    return cnt

def three(N):
    cnt = 0
    remain = 2
    if N >= 200 and N <= 229 and remain != 0:
        while N < 229 and remain != 0:
            N += 1
            cnt += 1
            remain -= 1
    return cnt 

def four(N):
    cnt = 0
    N += 1
    cnt += 1
    return cnt

arr = [one(N), two(N), three(N), four(N)]
print(arr.index(max(arr))+1)




