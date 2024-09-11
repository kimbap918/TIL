def sol(n):
    ans = ''
    for i in range(1, n + 1):
        ans += str(i)
    return(ans.find(str(n)) + 1)

n=int(input())
print(sol(n))