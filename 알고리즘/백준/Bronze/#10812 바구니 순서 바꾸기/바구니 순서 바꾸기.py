N, M = map(int, input().split())
buckets = [i for i in range(1, N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    # print(i, j, k)
    # 왼쪽부터 i번째 바구니부터 j번째 바구니의 순서를 회전, 기준바구니는 k바구니
    # 리스트에 1~10까지 원소를 넣어둔 다음 입력받은 바구니 순서에 맞추어서 슬라이싱 해준다.
    # i, j, k가 입력되면 ~i, j~k까지, i~k까지, j~에 맞추어서 슬라이싱 해준다.
    buckets = buckets[:i] + buckets[k:j+1] + buckets[i:k] + buckets[j+1:]
    # print(buckets[:i])
    # print(buckets[k:j+1])
    # print(buckets[i:k])
    # print(buckets[j+1:])
    # print(buckets)
    
print(*buckets)