# # 숫자 1을 걸려면 2초
# # 1칸당 1초씩 증가 2 = 3초.., 3 = 4초.., 4 = 5초..
# import sys

# a = sys.stdin.readline().rstrip().upper()
# b = 0

# for i in a:
#     if i in ["A", "B", "C"]:
#         b += 3
#     elif i in ["D", "E", "F"]:
#         b += 4
#     elif i in ["G", "H", "I"]:
#         b += 5
#     elif i in ["J", "K", "L"]:
#         b += 6
#     elif i in ["M", "N", "O"]:
#         b += 7
#     elif i in ["P", "Q", "R", "S"]:
#         b += 8
#     elif i in ["T", "U", "V"]: 
#         b += 9
#     elif i == ["W", "X", "Y", "Z"]:
#         b += 10
#     else:
#         b += 11
# print(b)

import sys

s = sys.stdin.readline().rstrip()
a = {3:["A", "B", "C"], 4:["D", "E", "F"], 5:["G", "H", "I"],
6:["J", "K", "L"], 7:["M", "N", "O"], 8:["P", "Q", "R", "S"],
9:["T", "U", "V"], 10:["W", "X", "Y", "Z"]
}
cnt = 0

for i in s:
    for j, k in a.items():
        if i in k:
            cnt += j
print(cnt)