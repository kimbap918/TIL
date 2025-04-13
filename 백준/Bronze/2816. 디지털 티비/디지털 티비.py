N = int(input())
arr = [input() for _ in range(N)]
result = []

def move_to(index):
    # 현재 화살표는 맨 위(0번)에 있다고 가정
    return ['1'] * index

def move_up(i):
    res = []
    while i > 0:
        res.append('4')   # 현재 선택한 채널을 위로 올린다
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        i -= 1
    return res

# Step 1: KBS1을 맨 앞으로
kbs1_index = arr.index("KBS1")
result += move_to(kbs1_index)
result += move_up(kbs1_index)

# Step 2: KBS2를 두 번째로
# (KBS1이 앞으로 와서 인덱스가 바뀌었을 수 있음 → 다시 찾아야 함)
kbs2_index = arr.index("KBS2")
result += move_to(kbs2_index)
result += move_up(kbs2_index - 1)  # 두 번째 위치로 만들려면 인덱스 1이 되게 해야 함

print("".join(result))
