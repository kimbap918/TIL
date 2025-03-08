def potato_sum(C, potato):
    potato.sort(reverse=True)

    def backtrack(index, current_sum):
        if current_sum == C:
            return True
        if current_sum > C or index >= len(potato):
            return False

        if backtrack(index+1, current_sum+potato[index]):
            return True
        if backtrack(index+1, current_sum):
            return True

        return False

    return backtrack(0, 0)

P = int(input())


for i in range(P):
    arr = list(map(int, input().split()))
    K, C, potato = arr[0], arr[1], arr[2:]

    res = "YES" if potato_sum(C, potato) else "NO"
    print(K, res)
    

