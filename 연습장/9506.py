while True:
    n = int(input())
    cnt = 0
    ans = []
    if n == -1:
        break
    while n != cnt:
        cnt += 1
        # print(cnt)
        if n % cnt == 0:
            ans.append(cnt)
    # print(ans)
    ans = ans[:-1]
    if sum(ans) == n:
        print(f'{n} = 1 ', end = '')
        for j in ans[1:]:
            print(f'+ {j} ', end = '')
        print()
        # print(str(n) + " = ")
    else:
        print(str(n) + " is NOT perfect.")