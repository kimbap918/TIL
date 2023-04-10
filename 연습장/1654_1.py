import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
start, end = 1, max(lines)

def binary_search(start, end):
    while start <= end:
        mid = (start+end)//2
        line = 0
        for i in lines:
            line += i // mid
        if line >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(start, end))
