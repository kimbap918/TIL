# a, b = map(int, input().split())
# c = (a if (a>=b) else b)
# print(int(c))

# a, b, c = map(int, input().split())
# d = (a if (a<b) else b) if ((a if (a<b) else b) < c) else c
# print(d)

# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print(a)
# if b % 2 == 0:
#     print(b)
# if c % 2 == 0:
#     print(c)

# a, b, c = map(int, input().split())
# d = [a, b, c]
# for i in range(len(d)):
#     if d[i] % 2 == 0:
#         print("even")
#     elif d[i] % 2 == 1:
#         print("odd")

# a = int(input())
# if a < 0 and a % 2 == 0:
#     print("A")
# elif a < 0 and a % 2 == 1:
#     print("B")
# elif a > 0 and a % 2 == 0:
#     print("C")
# elif a > 0 and a % 2 == 1:
#     print("D")

# a = input()
# if a == "A":
#     print("best!!!")
# elif a == "B":
#     print("good!!")
# elif a == "C":
#     print("run!")
# elif a == "D":
#     print("slowly~")
# else:
#     print("what?")


# a = int(input())
# if a//3 == 0 or a//3 == 4:
#     print("winter")
# elif a//3 == 1:
#     print("spring")
# elif a//3 == 2:
#     print("summer")
# elif a//3 == 3:
#     print("fall")

# n = -1
# while n != 0:
#     n = int(input())
#     if n != 0:
#         print(n)

# n = int(input())
# while n != 0:
#     print(n)
#     n -= 1

# n = int(input())
# while n != 0:
#     print(n-1)
#     n -= 1

# c = ord(input())
# b = ord("a")
# while b <= c:
#     print(chr(b), end=' ')
#     b += 1

# a = int(input())
# b = 0
# while b <= a:
#     print(b)
#     b += 1

# a = int(input())
# b = 0
# for i in range(a+1):
#     print(b)
#     b += 1

# a = int(input())
# b = 0
# for i in range(a+1):
#     if i % 2 == 0:
#         b += i
# print(b)

# a = ""
# b = "q"
# while a != b:
#     a = input()
#     print(a)

# a = int(input())
# b = 0
# c = 0
# while b < a:
#     c += 1
#     b += c
# print(c)

# n, m = map(int, input().split())
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

# n = int(input(),16)
# for i in range(1, 16):
#     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='') 

# a = int(input())
# for i in range(1, a+1):
#     if i%10 == 3 or i%10 == 6 or i%10 == 9:
#         print("X", end=' ')
#     else:
#         print(i, end=' ')

# a, b, c = map(int, input().split())
# cnt = 0
# for i in range(a):
#     for j in range(b):
#         for k in range(c):
#             print(i, j, k)
#             cnt += 1
# print(cnt)

# h, b, c, s = map(int, input().split())
# print('{:.1f} MB'.format(h*b*c*s/8/1024/1024))

# w, h, b = map(int, input().split())
# print("{:.2f} MB".format(w*h*b/8/1024/1024))

# a = int(input())
# b = 0
# c = 0
# while True:
#     b += 1
#     c += b
#     if c >= a:
#         print(c)
#         break

# a = int(input())
# b = 0
# while a > b:
#     b += 1
#     if b % 3 == 0:
#         continue
#     print(b, end=' ')

# 등차수열
# a, d, n = map(int, input().split())
# for i in range(n-1):
#     a += d
# print(a)

# # 등비수열
# a, r, n = map(int, input().split())
# for i in range(n-1):
#     a *= r
# print(a)

# a, m, d, n = map(int, input().split())
# for i in range(n-1):
#     a = (a*m)+d
# print(a)

# d = 1
# a, b, c = map(int, input().split())
# while d%a != 0 or d%b != 0 or d%c != 0:
#     d+=1
# print(d)

# n = int(input())
# a = input().split()
# d = []
# for i in range(0, 24): # d 값(0) 저장
#     d.append(0)

# for i in range(n): # 출석 번호를 부를 횟수
#     a[i] = int(a[i]) # 횟수 저장

# for i in range(n):
#     d[a[i]] += 1

# for i in range(1, 24):
#     print(d[i], end='')

# n = int(input())
# a = input().split()
# d = []
# for i in range(0, 24): # d 값(0) 저장
#     d.append(0)

# for i in range(n-1, -1, -1): # 출석 번호를 부를 횟수
#     a[i] = int(a[i]) # 횟수 저장
#     print(a[i], end=' ')

n = int(input())
a = input().split()
fast = 10000
d = []
for i in range(0, 24): # d 값(0) 저장
    d.append(0)

for i in range(n-1, -1, -1): # 출석 번호를 부를 횟수
    a[i] = int(a[i]) # 횟수 저장
    if fast > a[i]:
        fast = a[i]
    print(fast)