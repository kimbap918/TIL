# 1. 이면수

# 숫자 4는 위대한 숫자 1과 시작의 숫자 3의 합으로
# “완벽하다”라는 의미를 갖는 완벽한 숫자이다. 
# 그와 동시에, 이 완벽한 숫자와 태초의 숫자들(2와 3)의 합으로
# 표현되는 숫자들, 즉 6, 7, 8, 9, 10 ... 들 역시 포함

# 즉, 4+ 2(or 3)으로 표현되는 수
# 4, 6, 7, 8, 9, 10 ..
# 과 더불어 각 자릿수의 합이 홀수여야 합


# 2. 임현수

# 그 숫자가 자체가 월드 문명의 chicken number(4) 혹은 
# starcraft number(2) 이거나 합성수이면서 소인수 분해를 했을때
# 소인수의 종류의 개수가 짝수개


# 3. 성경수 

# 이면수도, 임현수도 아닌 숫자


# 4. 이면수이면서 임현수 
import math

def is_imyeon(N):
    N_1 = str(N)
    summ = 0
    for i in N_1:
        summ += int(i)

    if (N == 4 or N >= 6) and (summ % 2 == 1):
        return True
    else:
        return False

def prime_factors(N):
    count = 0
    # 2로 나누어 떨어지는지 확인
    if N % 2 == 0:
        count += 1
        while N % 2 == 0:
            N //= 2

    # 3부터 √n 까지 홀수 소수 검사
    for i in range(3, int(math.sqrt(N))+1, 2):
        if N % i == 0:
            count += 1
            while N % i == 0:
                N //= i

    # 마지막으로 남은 소수가 있다면 (n > 1)
    if N > 1:
        count += 1
    
    return count

def is_composite(N):
    if N < 4:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return True
    return False

def is_imhyun(N):
    # chicken number(4) 또는 starcraft number(2)
    if N in {2, 4}:
        return True

    # 4미만이면 임현수가 아님
    if N < 4:
        return False

    # 합성수이면서 소인수의 개수가 짝수인지 확인
    return is_composite(N) and prime_factors(N) % 2 == 0

# 메인 로직
N = int(input())
one = is_imyeon(N)
two = is_imhyun(N)

# 결과 판정
if one and two:
    print(4)  # 이면수이면서 임현수
elif one:
    print(1)  # 이면수
elif two:
    print(2)  # 임현수
else:
    print(3)  # 성경수