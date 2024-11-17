acm=[]
cnt=0
anscnt=0
while 1:
    try:
        a,b,c=input().split()
        if c=='right': cnt+=acm.count(b)*20+int (a) ; anscnt+=1
        acm.append(b)
    except : break
print(anscnt, cnt)
