N = int(input())
study_plan = list(map(int, input().split()))
total_time = sum(study_plan) + (8 * (N-1))

d, t = total_time // 24, total_time % 24

print(d, t)