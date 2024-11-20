import sys
input = sys.stdin.readline

while True:
    T = input().rstrip()

    if T == "#":
        break
    
    if len(T) - T.count("A") <= T.count("A"):
        print("need quorum")
    elif T.count("Y") > T.count("N"):
        print("yes")
    elif  T.count("Y") < T.count("N"):
        print("no")
    elif T.count("Y") == T.count("N"):
        print("tie")

