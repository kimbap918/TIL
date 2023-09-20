def numCount(a, num): 
    ans = 0
    while a != 0: # a가 0이 나올때까지 
        a = a//num # a를 num으로 나눈 몫 구하기 n : 25//5 = 5, 5//5 = 1, 1//5 = 0
                   # m : 12//5 = 2, 2//5 = 0
                   # n-m : 13//5 = 2, 2//5 = 0
        ans += a # 5 + 1 = 6, 2,  2
    return ans

# 끝자리가 0이라는 것은 10의 배수
# 10은 2와 5로 구성되어 있음
# 2와 5 짝이 맞아야 10이 되므로 2의 개수와 5의 개수중 더 작은게 10의 개수이다.
n, m = map(int, input().split()) # 25, 12

five = numCount(n, 5) - numCount(m, 5) - numCount(n-m, 5) # 6 - 2 - 2
two = numCount(n, 2) - numCount(m, 2) - numCount(n-m, 2)

print(min(five, two))