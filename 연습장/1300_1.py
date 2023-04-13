import sys
input = sys.stdin.readline

N, K = int(input()), int(input())
start, end = 1, K

def binary_search(start, end):
    res = 0
    while start <= end:
        temp = 0
        mid = (start+end) // 2
        print("mid : "+str(mid))
        for i in range(1, N+1):
            temp += min(mid//i, N)
            print("mid // i : "+str(mid//i), ", N : "+str(N))
            print("temp : "+str(temp))
        if temp >= K:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res


print(binary_search(start, end))