# 다음과 같이 출력되게 해보자
# 유니코드 별 문자
word = '\u2B50'

N = int(input("별을 원하는 개수만큼 만들어봐요 : "))

# 반복문을 사용하여 별을 출력
for _ in range(N):
    print(word, end='')

print()  
