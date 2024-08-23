import sys
for _ in range(int(sys.stdin.readline())):
    tmp=[0]*26
    tmp2=[0]*26
    tmpstring=sys.stdin.readline()
    tmpstring2=sys.stdin.readline()
    for i in range(len(tmpstring)-1):
        tmp[ord(tmpstring[i])-97]+=1
    for i in range(len(tmpstring2)-1):
        tmp2[ord(tmpstring2[i])-97]+=1
    cnt=0
    for i in range(26):
        cnt+= abs(tmp[i]-tmp2[i])
    print("Case #%d: %d"%(_+1,cnt) )