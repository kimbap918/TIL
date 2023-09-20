import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
start, end = 1, K
# 3x3
# [1, 1] [1, 2] [1, 3]
# [2, 1] [2, 2] [2, 3]
# [3, 1] [3, 2] [3, 3]

# B = [1, 2, 3, 2, 4, 6, 3, 6, 9]
# B[k] = 6

# 3 * 3의 배열에서 7보다 작거나 같은 수 구해보기
# 1*1 ~ 1*7
# 2*1 ~ 2*3
# 3*1 ~ 3*2

# 1, 2, 3, 4, 5, 6, 7
# 2, 4, 6
# 3, 6 

# 7 // 1 = 7
# 7 // 2 = 3
# 7 // 3 = 2

# 

# 우리는 이분 탐색으로 어떤 수보다 작은 자연수의 곱(i * j)이 몇 개인지 알아낼 것이다.
# A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.
# 위 수가 존재할텐데, 이는 반대로 생각해보면 20을 행으로 나눈 몫이다.

# 20//1: 10개 --> 단 열의 숫자(N*N배열이므로)를 초과할 수 없다.

# 20//2: 10개

# 20//3: 6개
# .
# .
# .
# 20//10: 2개

def binary_search(start, end):
    ans = 0
    while start <= end:
        mid = (start+end) // 2
        temp = 0
        for i in range(1, N+1):
            # mid 이하의 i의 배수나 최대 N까지
            temp += min(mid//i, N)
        if temp >= K:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans

print(binary_search(start, end))