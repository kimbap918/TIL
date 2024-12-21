N = int(input())
a = list(map(int, input().split()))

for j in range(0, len(a)-1):
    if a[j] > a[j+1]:
        print("no")
        break

else:
    print("yes")

def check_extreme_property():
    # 입력 받기
    n = int(input())
    a = list(map(int, input().split()))
    
    # 배열이 오름차순인지 확인
    for j in range(1, n):
        print(j)
        if a[j] < a[j - 1]:
            print("no")  # 조건 위반
            return
    
    print("yes")  # 조건 만족

# 함수 실행
check_extreme_property()
