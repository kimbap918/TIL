# 1*x + 3*y = -1
# 4*x + 1*y = 7   
# 
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if ((a*x) + (b*y) == c) and ((d*x) + (e*y) == f):
            print(x, y)

# while True:
#     ans_1 = 0
#     ans_2 = 0
#     x, y = 
#     if ans_1 == 1 and ans_2 == 1:
#         break
#     else:
        

