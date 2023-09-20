
# 최빈수 = 특정 자료의 분포 중 가장 많이 나온 값
# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3 일때 8이 최빈수다.
# 최빈수가 여러개일때 가장 큰 점수를 출력할것

T = int(input()) # 테스트 케이스의 수

for i in range(1, T+1):
    n = int(input()) # 테스트케이스의 번호
    most = {}
    number = map(int, input().split())

    for j in number:
        if j not in most: 
            most[j] = 1
        else:
            most[j] += 1

    result = sorted(most.keys(), reverse= True)
    print("#{} {}".format(n, max(result, key=most.get)))
