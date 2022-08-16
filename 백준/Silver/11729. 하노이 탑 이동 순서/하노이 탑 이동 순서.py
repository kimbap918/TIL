def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1) # 옮긴 횟수
hanoi_tower(n, 1, 3) # N = 원판의 개수, 1번장대, 3번장대로 이동