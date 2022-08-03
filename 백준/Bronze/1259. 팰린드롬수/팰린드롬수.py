def rev(n):
    a = ""
    for i in range(len(n)-1, -1, -1):
        a += n[i]
    return a

while True:   
    N = input()
    A = rev(N)  
    if N == "0":
        break
    if N == A:
        print("yes")
    else:
        print("no")
