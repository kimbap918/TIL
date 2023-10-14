T = int(input())
for _ in range(T):
    q = input()
    N = int(input())
    li = [int(input()) for i in range(N)]
    print("YES" if sum(li)%N == 0 else "NO")