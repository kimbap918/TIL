n=int(input())
for i in range(n):
    a=input()
    score=0
    for j in a:
        if j == " ":
            continue
        else:
            a_score=ord(j)-64
            score+=a_score
    if score==100:
        print('PERFECT LIFE')
    else:
        print(score)