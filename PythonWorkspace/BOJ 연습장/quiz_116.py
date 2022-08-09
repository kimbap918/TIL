T = int(input())
a = []
for _ in range(T):
    S = input()

    for i in range(len(S)-1, -1, -1):
       a.append(S[i])
    s = ''.join(a)
    s1 = list(s.split())
    a = []
    for j in range(len(s1)-1, -1, -1):
        print(s1[j].rstrip(), end = ' ')
    
        
for i in range(T):
    string = list(input().split())
    for j in string:
        print(j[::-1], end = ' ')