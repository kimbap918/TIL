import sys
from collections import Counter

N = int(sys.stdin.readline().strip())  # 첫 번째 입력을 받아서 N 설정

for _ in range(N):
    A, B = sys.stdin.readline().strip().split()
    
    if len(A) != len(B):  # 길이가 다르면 불가능
        print("Impossible")
        continue

    # 두 단어의 문자 빈도 비교
    if Counter(A) == Counter(B):
        print("Possible")
    else:
        print("Impossible")
