N = int(input())
a = list(map(int, input().split()))  # 입력 값을 정수형으로 변환

for j in range(0, len(a)-1):
    if a[j] > a[j+1]:
        print("no")
        break
else:
    print("yes")
