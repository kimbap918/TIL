A, B = map(int, input().split())
# 최대공약수? 두 수에 대해 나눠지는 수 중에 제일 높은 수
# 최소 공배수 두 수를 곱할 때 같아지는 수 중 최소 수
# 유클리드 호제법으로 최대공약수 구하기
result = []

def GCD(x, y):
    while(y):
        x, y = y, x%y
        min = A*B/x
    print(x)
    print(int(min))
    
GCD(A, B)

