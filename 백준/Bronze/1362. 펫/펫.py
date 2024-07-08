from sys import stdin
input = stdin.readline

scene_num = 0
state = [":-)", ":-(", "RIP"]

while (n:=input().split()) != ["0", "0"]:
    o, w = map(int, n)
    while (m:=input().split()) != ["#", "0"]:
        if w > 0:
            if m[0] == "F":
                w += int(m[1])
            else:
                w -= int(m[1])
                
    scene_num += 1
    if (o * 0.5) < w < (o * 2):
        print(scene_num, state[0])
    elif w <= 0:
        print(scene_num, state[2])
    else:
        print(scene_num, state[1])