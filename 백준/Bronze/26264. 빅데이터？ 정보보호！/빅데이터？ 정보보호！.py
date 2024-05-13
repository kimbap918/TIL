import sys

input = sys.stdin.readline

big = "bigdata"
sec = "security"

N = int(input())
words = input()

cnt_1 = words.count(big)
cnt_2 = words.count(sec)

if cnt_1 > cnt_2:
    print("bigdata?")
elif cnt_1 < cnt_2:
    print("security!")
else:
    print("bigdata? security!")