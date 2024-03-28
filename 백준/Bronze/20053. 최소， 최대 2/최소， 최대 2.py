t = int(input()) #테스트케이스

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min(arr),max(arr))