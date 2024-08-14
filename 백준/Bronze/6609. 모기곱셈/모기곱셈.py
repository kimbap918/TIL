while 1:
    try:
        m,p,l,e,r,s,n=map(int,input().split())
        for i in range(n):
            sum=m
            m=p//s
            p=l//r
            l=sum*e
        print(m)
    except:
        break