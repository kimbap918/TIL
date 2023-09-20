import sys
input = sys.stdin.readline
n, k, m = map(int, input().split())

# 1. 원래의 N과 K를 M으로 나눈 나머지를 구한다.
# 2. 구한 두 수가 각각 n0, k0가 된다.
# 3. n과 k를 m으로 나눈 몫을 구한다.
# 4. 그 몫으로 다시 m으로 나눈 나머지를 구하고 이번에는 두 수가 n1, k1이 된다
# 5. 이들 두 수가 모두 0이 될때까지 반복한다.
# 6. 모든 nCk를 곱하고 나머지 연산을 적용한다.

# 이때 중요한점은 Ni < k1가 될 수 있는데 이때는 0으로 계산해주어야한다.

# n의 % m 계산한 값을 담을 리스트
ni = []
# k의 % m 계산한 값을 담을 리스트
ki = []
# nCk = n! / (k! * (n-k)!)
# n 100 k 45 m 13
# 100 % 13 = 9, 45 % 13 = 6 / n0 = 9, k0 = 6
# 9C6 = 9! / (6! * (9-6)!) = 84 / m = 나머지 6
# 100 // 13 = 7, 45 // 13 = 3 
# 7C3 = 7! / (3! * (7-3)!) = 35 / m = 나머지 9
# 나머지 6, 9 를 곱함 = 54 % 13 = 2
# 정답 2

def bin(n, k):
    a = 1
    if (n < k):
        return 0
    elif n == k:
        return 1

    for i in range(1, k+1):
        a *= (n-i+1)
        a //= i
    return a

# 0이 될때까지 n%m, k%m 을 저장하고 나눈 몫을 갱신 
while(n != 0 or k != 0):
    ni.append(n % m)
    ki.append(k % m)
    n //= m
    k //= m

ans = 1
for i in range(len(ni)):
    # 모든 nCk를 곱하고 나머지연산
    ans *= bin(ni[i], ki[i])
    ans %= m 

print(ans)
# 음이 아닌 정수 n, k, p(p는 소수)에 대해 nCk mod p를 구하는 효율적인 계산방식을 제공하는 정리다.
# nCk = n! / k!(n-k)! 이므로 k가 클때 계산하기 매우 부담스럽다.
# nCk = (n-1 / k-1) + (n-1 / k) 를 이용해서 파스칼 삼각형을 구하거나 메모제이션방식으로 얻게 된다.