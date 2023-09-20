A, B = map(int, input().split())
ans = 0

# print(bin(2)[2:])
for i in range(A, B+1):
    num = str(bin(i)[2:])
    ans += num.count('1')
    
print(ans)


# print(bin(3))