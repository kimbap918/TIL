X, Y = map(int, input().split())
Z = Y*100 // X


def cal(N):
    nZ = (Y+N) * 100 // (X+N)
    if nZ > Z:
        return True
    return False

def binary_search(start, end):
    while start <= end:
        mid = (start+end) // 2
        if cal(mid):
            end = mid - 1
        else:
            start = mid + 1
    return start

if Z >= 99:
    print(-1)
else:
    print(binary_search(1, 1000000000))
