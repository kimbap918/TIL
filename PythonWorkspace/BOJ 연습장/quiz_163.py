# def merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
#     if (p < r) then {
#         q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
#         merge_sort(A, p, q);      # 전반부 정렬
#         merge_sort(A, q + 1, r);  # 후반부 정렬
#         merge(A, p, q, r);        # 병합
#     }
# }
