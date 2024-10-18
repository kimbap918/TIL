specialString='!@#$%^&*()-+'
n=int(input())
s=input()
tmp=[1,1,1,1]
for i in s:
    if ord(i)>=48 and ord(i)<=57: tmp[0]=0
    elif ord(i)>=65 and ord(i)<=91 : tmp[1]=0
    elif ord(i)>=97 and ord(i)<=123: tmp[2]=0
    elif i in specialString : tmp[3]=0
n+=sum(tmp)
if n >6 : print(sum(tmp))
else: print(sum(tmp)+ 6-n)