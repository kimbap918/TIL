N, K = map(int, input().split())

circle = [i for i in range(1, N+1)]
arr = []
index = 0


while circle:
    index = (index + K-1) % len(circle)
    arr.append(circle.pop(index))
# 결과 출력
print("<" + ", ".join(map(str, arr)) + ">")


# # 1, 2, 3, 4, 5, 6, 7
# -> 3
# # 1, 2, 4, 5, 6, 7 
# -> 6
# # 1, 2, 4, 5, 7 
# -> 2
# # 1, 4, 5, 7 
# -> 7
# # 1, 4, 5
# -> 5
# # 1, 4
# -> 1
# # 4
# -> 4
