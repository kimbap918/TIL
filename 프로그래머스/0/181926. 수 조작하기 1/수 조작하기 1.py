def solution(n, control):
    for com in control:
        if com == "w":
            n += 1
        elif com == "s":
            n -= 1
        elif com == "d":
            n += 10
        elif com == "a":
            n -= 10
    
    return n