while True:
    A,B,C,D=map(int,input().split())
    if A+B+C+D==0: break
    else: k=(B*C-A)//D;p=(B*C-A)%D;print([(k+1,k)[p==0],0][k<0])