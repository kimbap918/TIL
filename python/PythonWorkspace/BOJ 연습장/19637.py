import sys
input = sys.stdin.readline


def bin_search(arr, target):
    left, right = 0, len(arr)-1
    ans = len(arr)

    while left <= right:
        mid = (left+right) // 2
        if target <= arr[mid]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans



N, M = map(int, input().split())
# N = 칭호의 개수, M = 캐릭터의 개수
ns = []

for _ in range(N):
    name, power = list(map(str, input().rstrip().split()))
    ns.append((int(power), name))

# ns.sort()

limits = [power for power, _ in ns]
names = [name for _, name in ns]

for _ in range(M):
    power = int(input())
    idx = bin_search(limits, power)
    print(names[idx])

    
