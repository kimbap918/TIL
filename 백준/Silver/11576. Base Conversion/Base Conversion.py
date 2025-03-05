
# 17 8 # 17 진법을 8진법으로
# 2 # 2개
# 2 16 # 2와 16

# A진수를 10진수로 변환
# 10진수를 B진수로 변환

def convert_base(A, B, arr):
    decimal = 0
    power = 0
    
    # A진수를 10진수으로 변환
    # 리스트를 역으로 계산해서 승수를 올리는 방식으로 계산
    for digit in reversed(arr):
        # 예를 들어, 8진수 35를 10진수로 변환할때
        # 35 = 8**1 x 3 + 8**0 x 5 = 29
        decimal += digit * (A ** power)
        power += 1
    
    if decimal == 0:
        return [0]
    
    b_base_digits = []
    
    # 10진수를 B진수로 변환
    while decimal > 0:
        b_base_digits.insert(0, decimal % B)
        decimal //= B
    
    return b_base_digits


A, B = map(int, input().split()) # 미래의 진법 A, 정이의 진법 B
m = int(input()) # A진법으로 나타낸 숫자의 자리수 개수
arr = list(map(int, input().split())) # A진법으로 나타낸 숫자의 자리수 개수

result = convert_base(A, B, arr)
print(*result)