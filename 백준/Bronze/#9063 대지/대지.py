n = int(input())
bucket_A = []
bucket_B = []

if n <= 1:
    A, B = map(int, input().split())
    print(0)
else:
    for i in range(n):
        A, B = map(int, input().split())
        bucket_A.append(A)
        bucket_B.append(B)
    long = max(bucket_A) - min(bucket_A)
    lat = max(bucket_B) - min(bucket_B)

    print(lat*long)
    # print(bucket_A)
    # print(bucket_B)
