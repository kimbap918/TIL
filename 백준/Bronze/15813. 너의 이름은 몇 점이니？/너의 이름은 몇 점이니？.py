count = int(input())

name = list(input())
ascii_list = []

for i in name:
    ascii_list.append(ord(i)-64)

print(sum(ascii_list))