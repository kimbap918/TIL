def fac(n):
    if n<=1:
        return 1
    return n*fac(n-1)

sum=0.0

print("n e")
print("- -----------")
for i in range(10):
    sum=1/fac(i)+sum
    if i==0 or i==1:
        print("%d %d"%(i,sum))
    elif i==2:
        print(i, end=" ")
        print(round(sum,9))
    else:
        print("%d %.9f" %(i,sum))
        