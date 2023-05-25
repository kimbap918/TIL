# 자주 실행하는 이벤트 정리
# 빈도수 -> sort, lambda
# M개의 테스트마다 주어지는 k개의 숫자 중에서 최다 등장한 정수를 찾는 문제
# 최다 등장한 정수가 같다면, 큰 정수에서 작은 정수로 출력
# 단, 주어지는 정수는 1이상, N이하이다.

# 1. 많은 카테고리화 된 자료를 저장 = 딕셔너리 자료형
# 2. 자료를 여러가지 기준에 따라 정렬 = lambda
# 3. 정렬된 자료 중 조건에 맞는 결과 출력 = 반복문?

# 4 4
# 4 1 2 3 4
# 4 1 2 3 4
# 4 1 2 3 4
# 4 1 2 3 4

from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# defaultdict 는 자료형을 미리 선언 가능하다
cnt = defaultdict(int)
print(cnt)



for _ in range(M):
    events = list(map(int, input().split()))
    print(events)
    for i in events[1:]:
        cnt[i] += 1

ans = []
res = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)
res = list(filter(lambda x : x[1] == res[0][1], res))

for i in res:
    print(i[0], end=' ')


# lambda x가 정렬 조건을 가지는데, x[1]을 오름차순으로 가지고, 값이 같다면 x[0]을 비교해서 정렬.
# 정렬된 값을 내림차순으로 뒤집는다.
# res = sorted(cnt.items(), key = lambda x : (x[1], x[0]), reverse=True)

# sort() 메소드는 앞에 데이터가 들어가서 lambda를 사용할때 데이터를 넣지않아도 됨
# sorted 의 반환값은 리스트 형태
# sorted(data, key = lambda x : x ...)
# data.sort(key = lambda x : x ...)

# filter 함수
# list에서 원하는 값만 추출
# filter(추출 조건, 대상) -> 조건에 lambda를 정의할 수 있음
# 여기서는 res[0][0]과 같은 것들을 뽑아줘야함

# res = list(filter(lambda x : x[1] == res[0][1], cnt))
# for i in res:
#     print(i[0], end='')

