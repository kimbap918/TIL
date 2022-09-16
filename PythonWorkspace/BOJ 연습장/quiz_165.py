n = int(input()) # 회의의 수 
time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
# 회의정보가 주어짐, 시작시간/끝시간 
# 가장 많은 회의의 수를 알기 위해서는 
# 1. 빨리 끝나는 회의 순으로 정렬이 되어야 함(끝나는 시간의 오름차순)
# 2. 끝나는 시간이 같을 경우에는 빨리 시작하는 순으로 정렬이 되어야함(시작하는 시간의 오름차순)
# -> 시작시간/끝시간 입력을 튜플에 담아 람다식으로 정렬한다. 
ans = 0
end = 0
for s, e in time: # 정렬된 time 튜플에서 s, e 순회
    if s >= end: # s가 end 보다 크거나 같으면
        ans += 1 # ans 1 증가 
        end = e # end = e
print(ans)
