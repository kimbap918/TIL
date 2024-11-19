n=int(input())
for i in range(n,0,-1):
    print(str(i)+" bottle"+("s" if i>1 else "")+" of beer on the wall, "+str(i)+" bottle"+("s" if i>1 else "")+" of beer.")
    print("Take one down and pass it around, "+(str(i-1)+" bottle"+("s" if i-1>1 else "")+" of beer on the wall.\n" if i-1>0 else "no more bottles of beer on the wall.\n"))
print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, "+str(n)+" bottle"+("s" if n>1 else "")+" of beer on the wall.")
