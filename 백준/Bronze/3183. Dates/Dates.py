import datetime
while 1:
    d,m,y=map(int,input().split())
    if d==0 and m==0 and y==0 :break
    try:
        datetime.date(y,m,d)
        print("Valid")
    except : print("Invalid")