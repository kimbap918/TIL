# 알파벳을 오름차순 정렬해서 이어서 출력한 뒤, 숫자를 모두 더한 값을 출력
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


S = input()
arr = []
num = 0
for word in S:
    # .isalpha()
    if word in num_list:
        num += int(word)
    else:
        arr.append(word)

arr.sort()

print(''.join(arr)+str(num))