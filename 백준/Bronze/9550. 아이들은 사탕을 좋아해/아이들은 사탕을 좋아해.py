for _ in range(int(input())):
    N, K = map(int,input().split())
    candy = list(map(int, input().split()))
    answer = 0
    
    for i in candy:
        answer += i // K
    print(answer)