answer = list(map(int, input()))
user_input = list(map(int, input()))

def fail():
    for i in range(4):
        if result[i] != 2:
            continue
        while True:
            temp = (user_input[i] + 1) % 10
            out = temp not in user_input
            user_input[i] = temp
            if out:
                break

def ball():
    if 1 not in result:
        return
    pos = []
    value = []
    for i in range(4):
        if result[i] != 0:
            pos.append(i)
            value.append(user_input[i])
    for i in range(len(pos)):
        if i == 0:
            user_input[pos[i]] = value[-1]
        else:
            user_input[pos[i]] = value[i - 1]

make_input_count = 0
while True:
    make_input_count += 1
    result = [2, 2, 2, 2]
    if user_input == answer:
        print(make_input_count)
        break

    for i in range(4):
        if user_input[i] in answer:
            if user_input[i] == answer[i]:
                result[i] = 0
            else:
                result[i] = 1
                
    fail()
    ball()