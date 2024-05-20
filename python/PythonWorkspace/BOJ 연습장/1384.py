group = 1
while True:
    N = int(input())
    if N == 0:
        break
    people = []
    for _ in range(N):
        message = input().split()
        people.append(message)
        # print(people)
    print(f'Group {group}')
    flag = True
    for i in range(N):
        if 'N' in people[i][1:]:
            flag = False
            for j in range(1, N):
                if people[i][j] == 'N':
                    print(f'{people[i-j][0]} was nasty about {people[i][0]}')

    if flag:
        print("Nobody was nasty")
    print()
    group += 1
        # for i, msg in enumerate(message[1:]):
        #     if "N" == msg:
        #         print(N-(i+1))

    


# Ann P N P P
# Bob P P P P
# Clive P P P P
# Debby P N P P
# Eunice P P P P