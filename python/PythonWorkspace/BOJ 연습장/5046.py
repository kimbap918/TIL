N, B, H, W = map(int, input().split())

min_fee = float('inf')  # 최소 비용을 큰 값으로 초기화

for _ in range(H):
    p = int(input())
    person = list(map(int, input().split()))

    # 각 주마다 참가할 수 있는지 확인
    for available in person:
        if available >= N:
            fee = p * N
            min_fee = min(min_fee, fee)

if min_fee <= B:
    print(min_fee)
else:
    print("stay home")
