sticks = [64]
X = int(input())
cnt = 0

while X != sticks:
    if sum(sticks) > X:
        short = min(sticks)
        sticks.remove(short)
        sticks.append(short//2)

        if sum(sticks) < X:
            sticks.append(short//2)

    else:
        break

print(len(sticks))