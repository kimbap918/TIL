def evaluate(result):
    result = result.replace(' ', '')
    return eval(result)

def dfs(N, result, current):
    if current > N:
        if evaluate(result) == 0:
            results.append(result)
        return

    for op in ['+', '-', ' ']:
        dfs(N, result + op + str(current), current+1)



T = int(input())

for _ in range(T):
    results = []
    N = int(input())
    dfs(N, '1', 2)


    for res in sorted(results):
        print(res)

    print()
