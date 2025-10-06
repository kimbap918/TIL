import sys
input = sys.stdin.readline

n = int(input())
dna = list(input().rstrip())
itp = {"AG":"C", "AC":"A", "AT":"G", "GC":"T", "GT":"A", "CT":"G", "GA":"C", "CA":"A", "TA":"G", "CG":"T", "TG":"A","TC":"G"}

a,b = "", dna.pop()
for _ in range(n-1):
    a = dna.pop()
    if a == b:
        continue
        
    b = itp[a+b]
print(b)