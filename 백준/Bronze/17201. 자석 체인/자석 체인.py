n=int(input())
s=input()
cnt=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:cnt=1;print("No");exit()
if cnt==0: print("Yes")