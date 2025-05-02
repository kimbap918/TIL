N, S = map(int, input().split())
arr = list(map(int, input().split()))

def find_min(N, S, arr):
    left = 0
    right = 0
    current_sum = 0
    min_length = 1e9
    # print(min_length)
    
    while True:
        if current_sum >= S:
            min_length = min(min_length, right-left)
            current_sum -= arr[left]
            left += 1
        elif right == N:
            break
        else:
            current_sum += arr[right]
            right += 1

    return min_length if min_length != 1e9 else 0

print(find_min(N,S,arr))