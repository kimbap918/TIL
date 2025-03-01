N = int(input())

for i in range(N):
    words = input()
    cnt = 1
    tmp = []

    for j in range(len(words)-1):
        if words[j] == words[j+1]:
            cnt += 1
        else:
            tmp.append(str(cnt) + " " + words[j] + " ")
            cnt = 1

    tmp.append(str(cnt) + " " + words[-1] + " ")
    print(''.join(tmp))
