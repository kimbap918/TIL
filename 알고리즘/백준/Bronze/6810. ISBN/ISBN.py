# 앞의 10자리 9780921418 고정, 뒤의 3자리 입력으로 추가
# 9780921418 1-3-sum은 91
# 91 + a*1 + b*3 + c*1
a = int(input())
b = int(input())
c = int(input())

print('The 1-3-sum is', 91 + a+b*3+c)