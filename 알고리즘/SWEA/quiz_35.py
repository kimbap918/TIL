
for _ in range(1, 11):
    T = int(input())
    queue = list(map(int, input().split()))
    i = 1
    
    while True:
        a = queue.pop(0)-i # 큐의 맨 처음 요소를 -i 시키고 빼낸다.
        if a <= 0: # a가 0이거나 작아지면 반복을 종료한다.
            a = 0
            queue.append(a)
            break
        queue.append(a) # 큐의 빼낸 요소를 뒤에다 붙인다.
        i += 1 # i를 1 증가시킨다.      
        if i > 5: # i가 5를 초과하면
            i = 1 # i를 1로 초기화시킨다.
    print("#{} {} {} {} {} {} {} {} {}".format(_, *queue))