# 1. 지민이가 가지고 있는 막대의 길이를 모두 더한다. 처음에는 64cm 막대 하나만 가지고 있다. 이때, 합이 X보다 크다면, 아래와 같은 과정을 반복한다.
# 2. 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
# 3 만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
# 4 이제, 남아있는 모든 막대를 풀로 붙여서 Xcm를 만든다.
# 23
# 64
# 32 -> 1
# 64 -> 1
# 23 -> 4
# 48 -> 2


sticks = [64]
X = int(input())
cnt = 0

while X != sticks:
    if sum(sticks) > X:
        short = min(sticks)
        sticks.remove(short)
        print("짧은 막대를 제거"+str(sticks))
        sticks.append(short//2)
        print("짧은 막대를 반으로 잘라서 추가"+str(sticks))


        if sum(sticks) < X:
            sticks.append(short//2)
            print("합이 X보다 작을때 "+str(sticks))

    else:
        break

print(len(sticks))