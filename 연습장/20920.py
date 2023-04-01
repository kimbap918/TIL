import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = dict()

for i in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in arr:
            arr[word][0] += 1
        else:
            arr[word] = [1, len(word), word]

ans = sorted(arr.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in ans:
    print(i[0])

# for k, v in arr.items():
#     print(k[0])
# while len(arr) != 0:
#     max = -1
#     key = ""
#     leng = -1
#     ascii_cd = 123
#     for k, v in arr.items():
#         if v > max:
#             max = v
#             key = k
#         if v == max:
#             if len(k) > leng:
#                 leng = len(k)
#                 key = k
#             if len(k) == leng:
                



#     ans.append(key)
#     arr.pop(key)

# # print(ans)
# print(arr)