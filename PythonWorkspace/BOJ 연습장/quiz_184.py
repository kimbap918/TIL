def merge_sort(A, p, r):
    # merge함수의 병합정렬 결과에 count증가와 
    # count와 K번째 수가 일치 할 경우 K번째 수를 저장한다.
    if(p < r and count <= K):
        q = (p + r) // 2 # q는 p, r의 중간 지점
        merge_sort(A, p , q) # 전반부 정렬
        merge_sort(A, q + 1, r) # 후반부 정렬
        merge(A, p, q, r) # 병합

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
    # count. result를 전역변수로 설정, 지역변수로 설정시 메모리와 시간 차지
    global count, result
    i, j = p, q + 1 # i = p, j = q+1
    tmp = []
  
    while i <= q and j <= r:
        if(A[i] <= A[j]):
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    # 왼쪽 배열 부분이 남은 경우
    while i <= q:
        tmp.append(A[i])
        i += 1
    # 오른쪽 배열 부분이 남은 경우
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i, t = p, 0
    # 결과를 A[p..r]에 저장
    while i <= r:
        A[i] = tmp[t]
        count += 1
        # K번째 수를 찾을 경우 리턴하는 코드를 추가
        # 루프 탈출을 하지 않으면 시간초과가 발생
        if count == K:
            result = A[i]
            break
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
result = -1
merge_sort(A, 0, N - 1)
print(result)