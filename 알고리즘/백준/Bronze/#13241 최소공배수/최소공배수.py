# 유클리드 호제법은 나눗셈만 반복해서 최대공약수(GCD)를 구할 수 있다.
A, B = map(int, input().split())
tmp = 0

# 최대공약수 구하기(유클리드 호제법)
# 유클리드 호제법은 두 수를 0이 될때까지 나누는 방법
def GCD(A, B):
    while B != 0:
        tmp = A % B
        A = B
        B = tmp
    return A

# 두 수 A와 B의 최소공배수는 A와 B의 곱을 A와 B의 최대공약수를 나눈 것과 같다.
def LCM(A, B):
    return (A * B) / GCD(A, B)

print(int(LCM(A, B)))